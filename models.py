from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name : str
    brand_name : str
    regular_price_value : int
    offer_price_value : int
    currency : str
    classification_l1 : str
    classification_l2 : str
    classification_l3 : Optional[str] = None
    classification_l4 : Optional  [str] = None
    image_url : str

class UpdateSchema(BaseModel):
    key : str
    value : str
    name : Optional[str] 
    brand_name : Optional[str]
    regular_price_value : Optional[int]
    offer_price_value : Optional[int]
    currency : Optional[str]
    classification_l1 : Optional[str]
    classification_l2 : Optional[str]
    classification_l3 : Optional[str] = None
    classification_l4 : Optional  [str] = None
    image_url : Optional[str]

class Delete(BaseModel):
    key : str
    value : str