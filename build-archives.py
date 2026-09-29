"""Build standalone upload archives from the exported public repository (Python 3)."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile


def encoded(value):
    return (json.dumps(value, indent=2) + "\n").encode()


def build(root, output, app_id=None):
    if app_id is not None and not re.fullmatch(r"plugin_asdk_app[_A-Za-z0-9-]+", app_id):
        raise ValueError("Use the actual plugin_asdk_app ID from your ChatGPT connection URL")
    plugin = root / "plugins" / "deaf-data"
    paths = ["LICENSE", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json",
             "plugin.json", "mcp.json", ".mcp.json",
             "skills/explore-data/SKILL.md", "skills/explore-data/references/conventions.md",
             "skills/interpret-comparison/SKILL.md", "skills/explain-metric/SKILL.md"]
    files = {}
    for name in paths:
        path = plugin / name
        if any(p.is_symlink() for p in [plugin, path, *path.parents]):
            raise ValueError("Symlinks are not accepted")
        files[name] = path.read_bytes()
    version = json.loads(files["plugin.json"])["version"]
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Invalid version")
    common = {p: b for p, b in files.items() if p.startswith("skills/") or p == "LICENSE"}
    claude = dict(common)
    claude.update({p: files[p] for p in [".claude-plugin/plugin.json", ".mcp.json"]})
    chatgpt = dict(common)
    manifest = json.loads(files[".codex-plugin/plugin.json"])
    manifest.pop("mcpServers", None)
    chatgpt[".codex-plugin/plugin.json"] = encoded(manifest)
    chatgpt["README.md"] = b"# Deaf Data Lab skills\n\nContains three skills. Connect Deaf Data Lab separately to use live tools.\nThis archive does not register an MCP connection.\n"
    archives = {"claude": claude, "chatgpt-skills": chatgpt,
                "portable": files}
    if app_id:
        bound = dict(chatgpt)
        manifest["apps"] = "./.app.json"
        bound[".codex-plugin/plugin.json"] = encoded(manifest)
        bound[".app.json"] = encoded({"apps": {"deaf-data-lab": {"id": app_id, "required": True}}})
        bound["README.md"] = b"# Deaf Data Lab\n\nThree skills with a required registered ChatGPT MCP connection.\nThe registered connection must be accessible to the installing account.\n"
        archives["chatgpt-connected"] = bound
    output.mkdir(parents=True, exist_ok=False)
    sums = []
    for target, contents in archives.items():
        name = f"deaf-data-{version}-{target}.zip"
        with zipfile.ZipFile(output / name, "x", compression=zipfile.ZIP_DEFLATED) as archive:
            for path, data in sorted(contents.items()):
                info = zipfile.ZipInfo(path, (2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, data)
        sums.append(f"{hashlib.sha256((output / name).read_bytes()).hexdigest()}  {name}")
    (output / "SHA256SUMS").write_text("\n".join(sums) + "\n")
    return sorted(archives)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="New output directory")
    parser.add_argument("--chatgpt-app-id", help="Optional real registered ChatGPT app ID")
    args = parser.parse_args()
    print("Built: " + ", ".join(build(Path(__file__).resolve().parent, args.output, args.chatgpt_app_id)))
