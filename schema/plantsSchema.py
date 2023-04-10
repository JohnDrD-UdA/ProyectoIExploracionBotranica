from pydantic import BaseModel
from typing import Optional

class plant(BaseModel):
    id: Optional[str]
    common_name :str
    scientific_name  :str
    description : str
    height : int
    isPousonous : Optional[bool]
    isEatable : Optional[bool]
    hasFlowers : Optional[bool]
    produceFruits : Optional[bool]
    isShadePlant : Optional[bool]
    isSunPlant : Optional[bool]