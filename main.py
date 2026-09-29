from fastapi import FastAPI
import json
from fastapi import Path,Query,HTTPException

app = FastAPI()

def load_data():
    with open('teachers.json', 'r') as f:
        data = json.load(f)
        return data


@app.get('/')  # define route
def Chatbot():
    return {'message': 'Chatbot system'}


@app.get('/teachers')
def teachers():
    data=load_data()
    return data 

# Path params------------------------------------------

# If our data in the form of dict the we can use this code

# @app.get('/teachers/{teacher_id}')
# def view_teachers(teacher_id):
#     data=load_data() #load the all data
#     if teacher_id in data:
#         return data[teacher_id]
#     else:
#         return {'message': 'Teacher not found'} 
        
#  but our data is in the form of list/array so we use this code

@app.get('/teachers/{teacher_id}')
def view_teachers(teacher_id:str=Path(
    ...,
    description="Enter the teacher id",
    example='P001'
    )):
    data=load_data() #load the all data
    for teacher in data:
        if teacher['id'] == teacher_id:
            return teacher
    raise HTTPException(status_code=404, detail="Teacher not found")

    
# @app.get('/sort')
# def sort_teachers(sort_by:str=Query(...,description='sort on the basis of experience'),
# order:str=Query(...,description='ascending or descending order')): 
#     valid_fields=['experience']
#     if sort_by not in valid_fields:
#         raise HTTPException(status_code=400, detail="Invalid field select from experience")    
#     valid_order=['asc','desc']
#     if order not in valid_order:
#         raise HTTPException(status_code=400, detail="Invalid order select between asc and desc")    
#     data=load_data()
#     sorted_data=sorted(data,key=lambda x:x[sort_by],reverse=True if order=='desc' else False)
#     return sorted_data    


@app.get("/sort")
def sort_teachers(
    sort_by: str = Query(
        ...,
        description="Sort on the basis of experience"
    ),
    order: str = Query(
        ...,
        description="Ascending or descending order"
    )
):
    valid_fields = ["experience"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail="Invalid field. Select from experience"
        )

    valid_order = ["asc", "desc"]

    if order not in valid_order:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Select between asc and desc"
        )

    data = load_data()
    sorted_data = sorted(
        data,
        key=lambda x: x[sort_by],
        reverse=(order == "desc")
    )

    return sorted_data