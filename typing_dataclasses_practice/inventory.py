from dataclasses import dataclass
from enum import StrEnum


class ProductCategory(StrEnum):
    TECH = "TECH"
    FURNITURE = "FURNITURE"
    BOOKS = "BOOKS"