import logging
from telegram.ext import ApplicationBuilder

from config import API_TOKEN
from handler_registry import HandlerRegistry


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def main():
    # Create instance of Application
    application = ApplicationBuilder().token(API_TOKEN).build()

    # Register handlers through HandlerRegistry
    handler_registry = HandlerRegistry(application)
    handler_registry.register_handlers()

    # Start bot
    application.run_polling()


if __name__ == '__main__':
    main()
