# Run the MCP Client

Before running this client be sure to have the server up and running.  For more info on that, see: [https://github.com/dazzaji/filesystem](https://github.com/dazzaji/filesystem)

#### Step 1: Create the Virtual Environment and Install Dependencies Correctly

Use the following commands:
    
    ```bash
    mkdir mcp-client-py
    cd mcp-client-py
    ```
    
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

    ```bash
    pip install -r requirements.txt
    ```

This creates a virtual environment, activates it, and then installs `mcp` and `python-dotenv` (and their dependencies) into that environment.

### Step 2: Confirm or Correct the Environment Variables in .env

Create a `.env` file with your server path and the allowed directory. You can also specify tool and args for testing purposes.
   ```env
      SERVER_PATH=/Users/dazzagreenwood/filesystem/dist/index.js
      ALLOWED_DIRECTORY=/Users/dazzagreenwood/mcp-hello/module1/files
      
     # Test with arguments:
      #TOOL=list_directory
      #ARGS='{"path": "/Users/dazzagreenwood/mcp-hello/module1/files", "recursive": true}'
      
      # Or test with other tools
      #TOOL=read_file
      #ARGS='{"path": "/Users/dazzagreenwood/mcp-hello/module1/files/test.txt"}'
   ```

### Step 3: Running the Python Client

Run your client to test the server.

   ```bash
    python client.py
    ```
   *   If you used the optional `TOOL` and `ARGS` add those arguments like so:
    ```bash
        python client.py --tool "list_directory" --args '{"path": "/Users/dazzagreenwood/mcp-hello/module1/files", "recursive": true}'
    ```
This will:

*   Connect to your filesystem server.
*   List available tools.
*  Call the `write_file` to create a test file with text content in the specified directory, if `tool` is not specified in the .env file.
*   Display the results to the console.

### Step 4: Verifying Results

After successfully running the client, check the following:

1.  **Client Output:** You should see output like `Available tools: [ ... ]`, and the result from the `write_file` (or other tool call).
2.  **File Creation:** Verify that `testfile.txt` has been created with the correct content inside `/Users/dazzagreenwood/mcp-hello/module1/files/`.  If testing with the read or list tools, make sure the output is what you'd expect.

### Testing Workflow

Here are steps to verify the project with the client and a server:

#### Starting the Server
1.  **Open a Terminal**. You will need to start the server from a terminal.
2.  **Navigate to Server Directory**. Change directory to the folder containing the server:
    ```
    cd /Users/dazzagreenwood/filesystem
    ```
3.  **Run the Server:**
    ```bash
    node dist/index.js "/Users/dazzagreenwood/mcp-hello/module1/files"
    ```
    *   Replace `/Users/dazzagreenwood/filesystem/dist/index.js` with the actual path to the compiled file.
    *   Replace `/Users/dazzagreenwood/mcp-hello/module1/files` with the allowed directory.

#### Testing with the Client

1.  **Open another Terminal window** or split your existing terminal tab.
2.  **Navigate to Client Directory** Change directories into the `mcp-client-py` folder:
     ```bash
     cd /Users/dazzagreenwood/mcp-client-server/mcp-client-py
     source .venv/bin/activate
     ```
3. **Run the Client in Default Mode:**
    To test basic connectivity and the `write_file` tool:
    ```bash
     python client.py
    ```
     This will attempt to call write file, to create a file named test.txt into the `/Users/dazzagreenwood/mcp-hello/module1/files` directory with the string `Hello from Python the new standup MCP client!` as it's content.

4.  **Run the client with specific tools and arguments**: To test list_directory, use the following:
  ```bash
      python client.py --server-path /Users/dazzagreenwood/filesystem/dist/index.js --allowed-dir /Users/dazzagreenwood/mcp-hello/module1/files --tool list_directory --args '{"path": "/Users/dazzagreenwood/mcp-hello/module1/files", "recursive": true}'
  ```
    To test the `read_file` tool use:
  ```bash
   python client.py --server-path /Users/dazzagreenwood/filesystem/dist/index.js --allowed-dir /Users/dazzagreenwood/mcp-hello/module1/files --tool read_file --args '{"path": "/Users/dazzagreenwood/mcp-hello/module1/files/test.txt"}'
  ```
    * Replace the paths in the examples above to correspond to your local paths.

If setup correctly you should see the output that confirms each of these actions.

By following these instructions, you can now test your MCP server and client with various tools using Python and TypeScript/Node.js!
