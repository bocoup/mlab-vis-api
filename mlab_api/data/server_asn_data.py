# -*- coding: utf-8 -*-
'''
Data class for accessing data for API calls.
'''
from mlab_api.data.table_config import get_table_config
from mlab_api.constants import TABLE_KEYS
from mlab_api.data.base_data import Data
import mlab_api.data.bigtable_utils as bt
import mlab_api.data.data_utils as du

class ServerAsnData(Data):
    '''
    Connect to BigTable and pull down data.
    '''

    def get_server_metrics(self, server_id, timebin, starttime, endtime):
        '''
        Get data for specific location at a specific
        frequency between start and stop times.
        '''

        table_config = get_table_config(self.table_configs, timebin, TABLE_KEYS["servers"])

        location_key_fields = du.get_key_fields([server_id], table_config)
        formatted = bt.get_time_metric_results(location_key_fields, self.get_pool(), timebin, starttime, endtime, table_config, "servers")

        # set the ID to be the location ID
        # formatted["meta"]["id"] = server_id

        return formatted
