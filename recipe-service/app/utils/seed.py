from ..db.models import Recipe 
from sqlalchemy.orm import Session 
from pathlib import Path

base_dir = Path(__file__).resolve().parent 
file_path = base_dir/"seed.txt"

data = []
with open(file_path, 'r') as f:
    content = f.read()
    for i, item in enumerate(content.splitlines()): 
        iter_7 = i % 7
        if iter_7 == 0:
            name = item.split('-')[1]
        if iter_7 == 1:
            calorie = int(item.split('-')[1])
        if iter_7 == 2:
            nutriscore = int(item.split('-')[1])
        if iter_7 == 3:
            rating = item.split('-')[1]
        if iter_7 == 4: 
            voting = item.split('-')[1]
        if iter_7 == 5:
            tags = item.split('-')[1]
        if iter_7 == 6:
            image = item.split('-')[1]
            data.append(
                Recipe(
                    name=name.strip(),calorie=calorie,nutriscore=nutriscore, rating=rating.strip(),voting=voting, 
                    tags=tags.strip(), image=image.strip())
            )


def seed_database(db: Session):
    if not db.query(Recipe).first():
        db.add_all(data)
        db.commit() 
    
    