from proto import snakes_pb2
from proto.proto_meta import MessageType, MessageFields


class ProtoMessages:
    def __init__(self) -> None:
        pass

    def create_announcement_message(self, game_name: str, can_join: bool,
                                     width: int, height: int, food_static: 
                                     int, delay: int, player_name: str, 
                                     player_id: int, player_role, player_score: int) -> bytes:
        
        msg = snakes_pb2.GameMessage()
        msg.msg_seq = 1001 
        
        announcement = msg.announcement
        
        game = announcement.games.add()  
        game.game_name = game_name
        game.can_join = can_join
        game.config.width = width
        game.config.height = height
        game.config.food_static = food_static
        game.config.state_delay_ms = delay
        
        player = game.players.players.add()
        player.name = player_name
        player.id = player_id
        player.role = snakes_pb2.MASTER
        player.score = player_score
        return msg.SerializeToString()

    def get_game_name(self, message):
        return message.announcement.games[0].game_name

    def get_message_type(self, message):
        if message.HasField(MessageType.ANNOUNCEMENT):
            return MessageType.ANNOUNCEMENT
    
    def deserialize(self, data: bytes):
        message = snakes_pb2.GameMessage()
        message.ParseFromString(data)
        return message



        


        
        
        
        


