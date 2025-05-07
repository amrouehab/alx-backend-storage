#!/usr/bin/env python3
"""Returns all students sorted by average score"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
