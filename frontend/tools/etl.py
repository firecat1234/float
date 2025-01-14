# etl_tools.py

from typing import Dict, List
from web_tools import fetch_webpage_content, extract_text_from_html, extract_links_from_html, extract_images_from_html
from api_tools import fetch_data_from_api, process_api_data
from services.memory_service import MemoryService

class ETLTools:
    def __init__(self):
        self.memory_service = MemoryService()

    def extract(self, source: Dict) -> Dict:
        """
        Extracts raw data from a source, either a web page or API.
        Input schema:
        {
            "type": "web" | "api",  # Source type
            "config": Dict           # Configuration for the source
        }
        """
        source_type = source.get("type")
        config = source.get("config", {})

        if source_type == "web":
            return fetch_webpage_content(config)
        elif source_type == "api":
            return fetch_data_from_api(config)
        else:
            return {"status": "error", "message": "Unsupported source type."}

    def transform(self, data: Dict, transform_config: Dict = None) -> Dict:
        """
        Transforms raw data into structured or processed formats.
        Input schema:
        {
            "type": "web" | "api",  # Data type
            "raw_data": str | List[Dict],  # Raw data to transform
            "config": Dict           # Transformation options
        }
        """
        data_type = data.get("type")
        raw_data = data.get("raw_data")

        if data_type == "web":
            html = raw_data
            if "extract_text" in transform_config and transform_config["extract_text"]:
                return extract_text_from_html({"html": html})
            elif "extract_links" in transform_config and transform_config["extract_links"]:
                return extract_links_from_html({"html": html})
            elif "extract_images" in transform_config and transform_config["extract_images"]:
                return extract_images_from_html({"html": html})
        elif data_type == "api":
            return process_api_data({"raw_data": raw_data, **transform_config})

        return {"status": "error", "message": "Unsupported data type for transformation."}

    def load(self, data: Dict) -> Dict:
        """
        Loads transformed data into memory or database.
        Input schema:
        {
            "type": "memory",  # Storage type
            "content": Dict     # Content to store
        }
        """
        storage_type = data.get("type")
        content = data.get("content")

        if storage_type == "memory":
            self.memory_service.store(content)
            return {"status": "success", "message": "Data stored in memory."}

        return {"status": "error", "message": "Unsupported storage type."}
