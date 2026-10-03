# hello_world_project

A minimal Python hello-world program with a pytest test suite, plus a walkthrough for setting up [Claude Code](https://code.claude.com/docs) to work on it.

## The project

| File | What it does |
| --- | --- |
| `hello.py` | `greet(name="World")` returns `"Hello, {name}!"`. Running the file prints `Hello, World!`. |
| `test_hello.py` | pytest tests for `greet()` and for running `hello.py` as a script. |

### Run it

Requires Python 3.8+.

```bash
python3 -m venv .venv
.venv/bin/pip install pytest

.venv/bin/python hello.py          # prints: Hello, World!
.venv/bin/python -m pytest -v      # runs the tests
```

On Windows, use `.venv\Scripts\python` instead of `.venv/bin/python`.

## Setting up Claude Code

Claude Code is Anthropic's AI coding assistant. It runs in your terminal, reads your project, edits files and runs commands with your approval.

### 1. Check the requirements

- **OS:** macOS 13+, Windows 10 (1809+), Ubuntu 20.04+, Debian 10+ or Alpine 3.19+
- **Hardware:** 4 GB+ RAM, x64 or ARM64 processor
- **Account:** a Claude Pro, Max, Team or Enterprise plan, or an Anthropic Console (API) account. The free claude.ai plan doesn't include Claude Code.
- An internet connection

### 2. Install

The native installer is recommended because it updates itself automatically.

**macOS, Linux, WSL:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

```batch
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

On native Windows, installing [Git for Windows](https://git-scm.com/downloads/win) is recommended so Claude Code can use Bash. Without it, Claude Code uses PowerShell instead.

<details>
<summary>Other install methods (Homebrew, WinGet, npm)</summary>

```bash
# Homebrew (macOS). Doesn't auto-update; run `brew upgrade claude-code` to update.
brew install --cask claude-code

# WinGet (Windows). Doesn't auto-update; run `winget upgrade Anthropic.ClaudeCode` to update.
winget install Anthropic.ClaudeCode

# npm (requires Node.js 22+). Don't use sudo.
npm install -g @anthropic-ai/claude-code
```

</details>

### 3. Verify the install

Open a **new** terminal window, then run:

```bash
claude --version
```

It should print a version number such as `2.1.288 (Claude Code)`. If you get `command not found`, the install directory (`~/.local/bin` on macOS/Linux) isn't on your `PATH` yet. See [Troubleshoot installation](https://code.claude.com/docs/en/troubleshoot-install).

For a fuller health check, run:

```bash
claude doctor
```

### 4. Log in

Start Claude Code from inside this project:

```bash
cd hello_world_project
claude
```

The first time, it opens your browser to sign in with your Claude account. Approve the login and return to the terminal.

If the `ANTHROPIC_API_KEY` environment variable is set, Claude Code asks once whether to use that key instead of opening the browser.

### 5. Try it on this project

Once the session starts, type requests in plain English. For example:

```text
> /init
> run the tests
> add a farewell() function to hello.py and write tests for it
```

`/init` creates a `CLAUDE.md` file describing the project. Claude Code reads it at the start of every session. Commit it so anyone else using Claude Code on this repo gets the same context.

Claude Code asks for permission before editing files or running commands. Review each request before you approve it.

### Useful commands

| Command | What it does |
| --- | --- |
| `/help` | Lists commands |
| `/init` | Generates a `CLAUDE.md` for the project |
| `/clear` | Starts a fresh conversation |
| `/config` | Opens settings |
| `claude update` | Updates Claude Code right away |
| `claude -c` | Continues your most recent conversation |

### Keeping it updated

Native installs update automatically in the background. To update right away, run `claude update`. Homebrew, WinGet and npm installs must be updated manually with the commands shown in step 2.

### More help

- [Quickstart](https://code.claude.com/docs/en/quickstart)
- [Setup reference](https://code.claude.com/docs/en/setup)
- [Troubleshooting](https://code.claude.com/docs/en/troubleshoot-install)
