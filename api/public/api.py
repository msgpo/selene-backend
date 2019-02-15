from flask import Flask
from flask_restful import Api
from selene.api import JSON_MIMETYPE, output_json

from public_api.endpoints.device_metrics import DeviceMetricsEndpoint
from .endpoints.device import DeviceEndpoint
from .endpoints.device_setting import DeviceSettingEndpoint
from .endpoints.device_skill import DeviceSkillEndpoint
from .endpoints.device_skills import DeviceSkillsEndpoint
from selene.api.base_config import get_base_config

from .endpoints.device_subscription import DeviceSubscriptionEndpoint
from .endpoints.open_weather_map import OpenWeatherMapEndpoint
from .endpoints.wolfram_alpha import WolframAlphaEndpoint

public = Flask(__name__)
public.config.from_object(get_base_config())
public_api = Api(public)
public_api.representations[JSON_MIMETYPE] = output_json

public_api.representations.update()

public_api.add_resource(DeviceSkillsEndpoint, '/device/<string:device_id>/skill')
public_api.add_resource(DeviceSkillEndpoint, '/device/<string:device_id>/userSkill')
public_api.add_resource(DeviceEndpoint, '/device/<string:device_id>')
public_api.add_resource(DeviceSettingEndpoint, '/device/<string:device_id>/setting')
public_api.add_resource(DeviceSubscriptionEndpoint, '/device/<string:device_id>/subscription')
public_api.add_resource(WolframAlphaEndpoint, '/wa')  # TODO: change this path in the API v2
public_api.add_resource(OpenWeatherMapEndpoint, '/owm/<path:path>')     # TODO: change this path in the API v2
public_api.add_resource(DeviceMetricsEndpoint, '/device/<string:device_id>/metric/<path:metric>')