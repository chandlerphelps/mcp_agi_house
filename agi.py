import os
from typing import Any
from fastmcp import FastMCP
from nova_act import NovaAct, ActResult
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

mcp = FastMCP("Minimal Nova Act MCP Server")


@mcp.tool()
async def buy_me_pistachios() -> ActResult:
    """
    Buys a bag of wonderful pistachios salt and vinegar 22 oz using credentials from environment variables.
    This tool will automate the process of logging in and buying a bag of wonderful pistachios salt and vinegar 22 oz.
    Returns information about the bought product including name, price, and expected delivery date.
    """
    # Get credentials from environment variables
    username = os.getenv("AMAZON_USERNAME")
    password = os.getenv("AMAZON_PASSWORD")
    nova_act_api_key = os.getenv("NOVA_ACT_API_KEY")

    return_schema = {
        "type": "object",
        "properties": {
            "product_name": {"type": "string"},
            "product_price_dollars": {"type": "number"},
            "delivery_date": {"type": "string"},
        },
        "required": ["product_name", "product_price_dollars", "delivery_date"],
    }

    if not all([username, password, nova_act_api_key]):
        raise ValueError(
            "Error: Amazon credentials or Nova Act API key not configured in environment variables."
        )

    def _sync_run():
        with NovaAct(
            starting_page="https://www.amazon.com",
            nova_act_api_key=nova_act_api_key,
            headless=False,
        ) as nova:
            nova.act("click on the 'sign in' button", timeout=60)

            nova.act(f"enter username '{username}'", timeout=60)

            nova.act("click continue", timeout=60)

            # # cancel the passkey sign in if it's there
            # nova.act("if there is a passkey sign in, click cancel", timeout=60)

            # print("Attempting to enter password...")
            # nova.act(f"enter password '{password}'", timeout=60)

            # nova.act("click 'Sign-In'", timeout=60)

            nova.act(
                "search for 'wonderful pistachios salt and vinegar 22 oz'", timeout=60
            )

            nova.act(
                "click 'wonderful pistachios salt and vinegar 22 oz'",
                timeout=60,
            )

            nova.act(
                "click buy now",
                timeout=60,
            )

            nova.act("click 'Place Order'", timeout=60)

            result = nova.act(
                "Return the product name, price, and expected delivery date of the product I just bought",
                schema=return_schema,
                timeout=60,
            )

            return result

    try:
        return await asyncio.to_thread(_sync_run)
    except Exception as e:
        import traceback

        print(f"An error occurred in buy_me_pistachios: {e}")
        print(traceback.format_exc())
        raise


if __name__ == "__main__":
    print("Starting MCP Server for Nova Act...")
    asyncio.run(mcp.run())
