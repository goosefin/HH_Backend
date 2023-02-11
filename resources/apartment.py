from crypt import methods
import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import login_required, current_user 
from flask_cors import CORS, cross_origin

apartments = Blueprint('apartments','apartments')

#INDEX
@apartments.route('/', methods=['GET'])
@login_required
def apartments_index():
    apartment_dicts = [model_to_dict(apartment) for apartment in current_user.apartments]
    return jsonify({
        'data':apartment_dicts,
        'message':f'Successfully found {len(apartment_dicts)} apartments',
        'status':200
    }), 200

#CREATE
@apartments.route('/', methods=['POST'])
@login_required
def create_apartment():
    payload = request.get_json()
    print(payload)
    new_apartment = models.Apartment.create(address=payload['address'],bedrooms=payload['bedrooms'],price=payload['price'],cats=payload['cats'],dogs=payload['dogs'],laundry=payload['laundry'],dishwasher=payload['dishwasher'],outdoor_space=payload['outdoor_space'],elevator=payload['elevator'],doorman=payload['doorman'],link=payload['link'],scheduled_showing=payload['scheduled_showing'],scheduled_showing_time=payload['scheduled_showing_time'],seen=payload['seen'],applied=payload['applied'], approved=payload['approved'],user=current_user.id) 
    apartment_dict = model_to_dict(new_apartment)
    return jsonify(
        data = apartment_dict,
        message='Successfully created apartment',
        status = 201
    ),201