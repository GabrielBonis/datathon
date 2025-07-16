import json
import os
from fastapi import APIRouter, HTTPException, Query

router = APIRouter()

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "arquivos")


def load_json(filename: str):
    path = os.path.join(BASE_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def dict_to_paginated_list(data_dict: dict, skip: int = 0, limit: int = 50):
    keys = list(data_dict.keys())
    total = len(keys)
    sliced_keys = keys[skip: skip + limit]
    items = [{k: data_dict[k]} for k in sliced_keys]
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": items
    }


@router.get("/applicants", tags=["arquivos"])
def get_applicants(skip: int = Query(0, ge=0), limit: int = Query(50, gt=0)):
    data = load_json("applicants.json")
    return dict_to_paginated_list(data, skip, limit)


@router.get("/prospects", tags=["arquivos"])
def get_prospects(skip: int = Query(0, ge=0), limit: int = Query(50, gt=0)):
    data = load_json("prospects.json")
    return dict_to_paginated_list(data, skip, limit)


@router.get("/vagas", tags=["arquivos"])
def get_vagas(skip: int = Query(0, ge=0), limit: int = Query(50, gt=0)):
    data = load_json("vagas.json")
    return dict_to_paginated_list(data, skip, limit)
