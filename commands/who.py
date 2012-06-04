from numerics import RPL_WHOREPLY, RPL_ENDOFWHO

def run(client, line, serverhandler):
    if line.isMoreToRead():
        pattern = line.readWord()

    operatorsOnly = line.isMoreToRead()
    line.readToEnd()

    channel = serverhandler.getChannel(line.pattern) #TODO: Make this support more than just channels.
    if channel is None:
        return

    for channelMember in channel.members:
        flags = "H" #TODO: Work out why this should be G in some situations.

        if channelMember in channel.userModes['o']:
            flags += '@'

        if channelMember in channel.userModes['v']:
            flags += '+'

        client.sendNumeric(RPL_WHOREPLY, channel.name, channelMember.username, channelMember.hostname, serverhandler.config.servername, channelMember.nickname, flags, '0', channelMember.realname[1:])

    client.sendNumeric(RPL_ENDOFWHO, line.pattern)