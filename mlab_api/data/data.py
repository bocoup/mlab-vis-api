# -*- coding: utf-8 -*-
'''
Data instances to use in endpoints

Creates instances of necessary data classes for use in the application.
'''
import os
from mlab_api.data.location_data import LocationData
from mlab_api.data.client_asn_data import ClientAsnData
from mlab_api.data.server_asn_data import ServerAsnData
from mlab_api.data.search_data import SearchData
from mlab_api.data.raw_data import RawData
from mlab_api.data.table_config import read_table_configs
from mlab_api.data.bigtable_utils import init_pool

TABLE_CONFIGS = read_table_configs(os.environ.get('BIGTABLE_CONFIG_DIR'))

POOL = init_pool()

# Instances of data classes
LOCATION_DATA = LocationData(TABLE_CONFIGS, POOL)
CLIENT_ASN_DATA = ClientAsnData(TABLE_CONFIGS, POOL)
SERVER_ASN_DATA = ServerAsnData(TABLE_CONFIGS, POOL)
SEARCH_DATA = SearchData(TABLE_CONFIGS, POOL)
RAW_DATA = RawData(TABLE_CONFIGS, POOL)
