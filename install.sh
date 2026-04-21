#!/usr/bin/env bash
# ───��─────────────────────────────────────────────────────
# Agentic Substrate — One-Command Installer
# 安裝 Agentic Substrate 到 Claude Code 或 Cowork
# ─────────────────────────────────────────────────────────
#
# Usage 使用方式:
#   curl -fsSL https://raw.githubusercontent.com/ahnchen1983/agentic-substrate/main/install.sh | bash
#   — or 或者 —
#   git clone https://github.com/ahnchen1983/agentic-substrate.git && cd agentic-substrate && ./install.sh
#
# What this does 這個腳本做什麼:
#   1. Detects your Claude Code / Cowork skills directory
#      偵測你的 Claude Code / Cowork skills 目���
#   2. Copies all Skills to the right location
#      複製所有 Skills 到正確位置
#   3. Verifies installation
#      驗證安裝
#
# ─────────────────────────────────────────────────────────

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
BOLD='\033[1m'

echo ""
echo -e "${CYAN}╔��═════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║                                                  ║${NC}"
echo -e "${CYAN}║   ${BOLD}Agentic Substrate${NC}${CYAN}                              ║${NC}"
echo -e "${CYAN}║   The Foundational Architecture of               ║${NC}"
echo -e "${CYAN}║   LLM-Native Software                            ║${NC}"
echo -e "${CYAN}║                                                  ║${NC}"
echo -e "${CYAN}╚═════��═══════════════════════��════════════════════╝${NC}"
echo ""

# ─── Detect source directory ─────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ ! -d "${SCRIPT_DIR}/skills" ]]; then
    echo -e "${RED}Error: Cannot find skills/ directory.${NC}"
    echo "Make sure you're running this from the Agentic Substrate repo root."
    echo "確認你在 Agentic Substrate repo 根目錄執行此腳本。"
    exit 1
fi

if [[ ! -f "${SCRIPT_DIR}/.claude-plugin/plugin.json" ]]; then
    echo -e "${RED}Error: Cannot find .claude-plugin/plugin.json${NC}"
    echo "This doesn't look like a valid Agentic Substrate repo."
    exit 1
fi

# ─── Detect target directory ─────���───────────────────────
echo -e "${BLUE}Detecting installation target...${NC}"
echo -e "${BLUE}偵測安裝目標...${NC}"

# Option 1: Install as Claude Code plugin (project-level)
CLAUDE_PROJECT_DIR=".claude/plugins/agentic-substrate"

# Option 2: Install to user-level Claude Code skills
CLAUDE_USER_DIR="${HOME}/.claude/skills"

# Option 3: Custom path
TARGET_DIR=""

echo ""
echo -e "${BOLD}Where would you like to install?${NC}"
echo -e "${BOLD}你想安裝到哪裡？${NC}"
echo ""
echo "  [1] Current project (as Claude Code plugin)"
echo "      當前專案（作為 Claude Code 插件）"
echo "      → ${CLAUDE_PROJECT_DIR}/"
echo ""
echo "  [2] User-level Claude Code skills"
echo "      使用者層級 Claude Code skills"
echo "      → ${CLAUDE_USER_DIR}/"
echo ""
echo "  [3] Custom path"
echo "      自定義路徑"
echo ""
read -r -p "Choose [1/2/3] 選擇: " CHOICE

case "$CHOICE" in
    1)
        TARGET_DIR="${CLAUDE_PROJECT_DIR}"
        INSTALL_TYPE="plugin"
        ;;
    2)
        TARGET_DIR="${CLAUDE_USER_DIR}/agentic-substrate"
        INSTALL_TYPE="skills"
        ;;
    3)
        read -r -p "Enter path 輸入路徑: " CUSTOM_PATH
        TARGET_DIR="${CUSTOM_PATH}"
        INSTALL_TYPE="custom"
        ;;
    *)
        echo -e "${RED}Invalid choice. Exiting.${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${YELLOW}Installing to: ${TARGET_DIR}${NC}"
echo -e "${YELLOW}安裝到：${TARGET_DIR}${NC}"

# ─── Create directory and copy files ─────────────────────
mkdir -p "${TARGET_DIR}"

if [[ "$INSTALL_TYPE" == "plugin" ]]; then
    # Full plugin installation — include .claude-plugin/ and skills/
    echo -e "${BLUE}Installing as Claude Code plugin...${NC}"

    # Copy plugin config
    mkdir -p "${TARGET_DIR}/.claude-plugin"
    cp "${SCRIPT_DIR}/.claude-plugin/plugin.json" "${TARGET_DIR}/.claude-plugin/"

    # Copy all skills
    cp -r "${SCRIPT_DIR}/skills/"* "${TARGET_DIR}/skills/" 2>/dev/null || {
        mkdir -p "${TARGET_DIR}/skills"
        cp -r "${SCRIPT_DIR}/skills/"* "${TARGET_DIR}/skills/"
    }

    # Copy docs for reference
    if [[ -d "${SCRIPT_DIR}/docs" ]]; then
        cp -r "${SCRIPT_DIR}/docs" "${TARGET_DIR}/"
    fi

    # Copy Quick Start
    if [[ -f "${SCRIPT_DIR}/QUICK-START.md" ]]; then
        cp "${SCRIPT_DIR}/QUICK-START.md" "${TARGET_DIR}/"
    fi

else
    # Skills-only installation
    echo -e "${BLUE}Installing Skills...${NC}"
    echo -e "${BLUE}安裝 Skills...${NC}"

    # Copy each skill directory
    for skill_dir in "${SCRIPT_DIR}/skills/"*/; do
        if [[ -d "$skill_dir" ]]; then
            skill_name=$(basename "$skill_dir")
            echo -e "  ${GREEN}✓${NC} ${skill_name}"
            cp -r "$skill_dir" "${TARGET_DIR}/"
        fi
    done

    # Handle nested example skills
    if [[ -d "${SCRIPT_DIR}/skills/examples" ]]; then
        for example_dir in "${SCRIPT_DIR}/skills/examples/"*/; do
            if [[ -d "$example_dir" ]]; then
                example_name=$(basename "$example_dir")
                echo -e "  ${GREEN}✓${NC} examples/${example_name}"
            fi
        done
    fi
fi

# ─── Count installed skills ──────────────────────────────
SKILL_COUNT=$(find "${TARGET_DIR}" -name "SKILL.md" | wc -l | tr -d ' ')

# ─── Verify installation ─────────────────────────────────
echo ""
echo -e "${GREEN}╔════════════════════════════��═════════════════════╗${NC}"
echo -e "${GREEN}║  Installation complete! 安裝完成！                ���${NC}"
echo -e "${GREEN}╚════���══════════════════════════════���══════════════╝${NC}"
echo ""
echo -e "  ${BOLD}Location 位置:${NC}  ${TARGET_DIR}"
echo -e "  ${BOLD}Skills installed 已安裝:${NC}  ${SKILL_COUNT} Skills"
echo ""
echo -e "  ${CYAN}Installed Skills 已安裝的 Skills:${NC}"

find "${TARGET_DIR}" -name "SKILL.md" -print0 | while IFS= read -r -d '' skill_file; do
    skill_path=$(dirname "$skill_file")
    skill_name=$(basename "$skill_path")
    echo -e "    ${GREEN}✓${NC} ${skill_name}"
done

echo ""
echo -e "${BOLD}What's next? 下一步？${NC}"
echo ""
echo "  1. Open Claude Code or Cowork"
echo "     開啟 Claude Code 或 Cowork"
echo ""
echo "  2. Try saying: \"I want to discover my Skills\""
echo "     試著說：「我想發現我的 Skills」"
echo ""
echo "  3. Or: \"Help me build a Skill for my workflow\""
echo "     或者：「幫我為我的工作流程建一個 Skill」"
echo ""
echo -e "  ${BLUE}Read the Quick Start guide: QUICK-START.md${NC}"
echo -e "  ${BLUE}閱讀快速入門指南：QUICK-START.md${NC}"
echo ""
echo -e "${CYAN}Learn more: https://github.com/ahnchen1983/agentic-substrate${NC}"
echo ""
