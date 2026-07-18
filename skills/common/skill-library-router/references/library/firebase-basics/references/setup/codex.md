# Codex Setup

To get the most out of Firebase in Codex, follow these steps to install the agent skills and the MCP server.

## Recommended Method: Using Plugins

The recommended method is using the plugin marketplace to install both the agent skills and the MCP functionality.

### 1. Install and Verify Plugins

Check if the plugins are already installed before proceeding:

1. **Check Existing Skills**: Check the Codex skills folder or skills UI for `firebase-basics`. If your `npx skills` CLI supports Codex targets, use the Codex agent target for local and global checks.
2. **Check Existing MCP Configuration**: Check Codex MCP settings or run the Codex MCP list command if available. Note whether Firebase is configured.
3. **Determine Installation Path**:
   - If **both** skills and MCP configuration are found, the plugin is fully installed. **Stop here and skip all remaining setup steps in this document.**
   - If **neither** are found, proceed to step 4.
   - If **only one** is found (e.g., skills are installed but MCP is missing, or vice versa), **stop and prompt the user**. Explain the mixed state and ask if they want to proceed with installing the Firebase plugin before continuing to step 4.
4. **Add Marketplace**: Run the following command to add the marketplace (this uses the default User scope):
   ```bash
   codex plugin marketplace add firebase/agent-skills
   ```
5. **Install Plugins**: Run the following command to install the plugin:
   ```bash
   codex plugin install firebase@firebase
   ```
6. **Verify Installation**: Re-run the checks in steps 1 and 2 to confirm the skills and the MCP server are now available.

### 2. Restart and Verify Connection
1. **Restart Codex**: Instruct the user to restart Codex. **Stop and wait** for their confirmation before proceeding.
