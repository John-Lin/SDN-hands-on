from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls


class DeleteAll(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(DeleteAll, self).__init__(*args, **kwargs)

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath

        self.del_flows(datapath)

    def del_flows(self, dp):
        ofp = dp.ofproto
        parser = dp.ofproto_parser
        wildcard_match = parser.OFPMatch()
        instructions = []

        mod = parser.OFPFlowMod(datapath=dp, table_id=0,
                                command=ofp.OFPFC_DELETE,
                                out_port=ofp.OFPP_ANY,
                                out_group=ofp.OFPP_ANY,
                                match=wildcard_match,
                                instructions=instructions)
        dp.send_msg(mod)
