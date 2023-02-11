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