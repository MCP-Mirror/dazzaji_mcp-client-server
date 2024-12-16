import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import os
from dotenv import load_dotenv
import argparse
import json

load_dotenv()

async def main():
    parser = argparse.ArgumentParser(description="MCP Client for testing filesystem server")
    parser.add_argument("--server-path", help="Path to the MCP server file")
    parser.add_argument("--allowed-dir", help="Allowed directory for the server")
    parser.add_argument("--tool", help="Tool to call (e.g., write_file, read_file)")
    parser.add_argument("--args", help="Tool arguments as JSON string")
    
    args = parser.parse_args()
    
    # Get server path from args or environment
    server_path = args.server_path or os.environ.get('SERVER_PATH')
    if not server_path:
        print("Please provide server path via --server-path or SERVER_PATH env variable")
        exit(1)
    
    # Get allowed directory from args or environment
    allowed_dir = args.allowed_dir or os.environ.get('ALLOWED_DIRECTORY')
    if not allowed_dir:
        print("Please provide allowed directory via --allowed-dir or ALLOWED_DIRECTORY env variable")
        exit(1)

    print(f"Connecting to server at: {server_path}")
    print(f"Using allowed directory: {allowed_dir}")
    
    # Create server parameters for stdio connection
    server_params = StdioServerParameters(
        command="node",  # Using node since filesystem server is TypeScript
        args=[server_path, allowed_dir],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print("\nAvailable tools:", [tool.name for tool in tools])
            
            # If tool and args are provided, call the specified tool
            if args.tool and args.args:
                try:
                    tool_args = json.loads(args.args)
                    result = await session.call_tool(
                        name=args.tool,
                        arguments=tool_args
                    )
                    print(f"\n{args.tool} result:", result)
                except json.JSONDecodeError:
                    print("Error: Tool arguments must be valid JSON")
                except Exception as e:
                    print(f"Error calling tool: {e}")
            else:
                # Default test: write a test file
                print("\nRunning default test: write_file")
                test_file_path = os.path.join(allowed_dir, "test.txt")
                create_file_result = await session.call_tool(
                    name="write_file",
                    arguments={
                        "path": test_file_path,
                        "content": "Hello from Python the new standup MCP client!"
                    }
                )
                print('Write file result:', create_file_result)

if __name__ == "__main__":
    asyncio.run(main()) 