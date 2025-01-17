import importlib
from telegram.ext import ApplicationBuilder, CommandHandler

from handlers.start import start_handler


class HandlerRegistry:
    def __init__(self, application: ApplicationBuilder):
        self.application = application

    def register_handlers(self):
        handlers = ["start"]  # Modules list with handlers
        for handler_name in handlers:
            module = importlib.import_module(f"handlers.{handler_name}")
            handler = getattr(module, f"{handler_name}_handler")
            self.application.add_handler(handler)
