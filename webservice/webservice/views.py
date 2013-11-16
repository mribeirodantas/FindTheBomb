from django.http import HttpResponse
import string

def create_map(request, arguments):
    arguments = str(arguments)
    arguments = arguments.split("&")
    if len(arguments) != 2:
        reply =u"Exactly two values must be informed."
    else:
        reply = u"The map \"%s\" was created.<br> Welcome %s." % (arguments[0], arguments[1])
        # Make Marcel be in the map
    return HttpResponse(reply)

def join_CT(request, arguments):
    arguments = str(arguments)
    arguments = arguments.split("&")
    if len(arguments) != 2:
        reply =u"Exactly two values must be informed."
    # Check if map exists
    # Check if this name is already in use
    else:
        reply = u"Now you're a Counter Terrorist, %s.<br> Joining \"%s\".." % (arguments[0], arguments[1])
    return HttpResponse(reply)

def join_TR(request, arguments):
    arguments = str(arguments)
    arguments = arguments.split("&")
    if len(arguments) != 2:
        reply =u"Exactly two values must be informed."
    # Check if map exists
    # Check if this name is already in use
    else:
        reply = u"Now you're a Terrorist, %s.<br>Joining \"%s\".." % (arguments[0], arguments[1])
    return HttpResponse(reply)

def quit_match(request, arguments):
    reason = u"Not known"
    arguments = str(arguments)
    arguments = arguments.split("&")
    if len(arguments) != 3:
        reply =u"Exactly two values must be informed."
    else:
        if (arguments[2] == '0'):
            reason = u"Connection timed out"
        reply = u"%s left the game \"%s\". Reason: %s." % (arguments[1], arguments[0], reason)
    return HttpResponse(reply)

def plant_bomb(request, arguments):
    arguments = str(arguments)
    arguments = arguments.split("&")
    if len(arguments) != 3:
        reply =u"Exactly three values must be informed."
    else:
        reply = u"The bomb was planted at %s:%s in the map \"%s\"" % (arguments[0], arguments[1], arguments[2])
    return HttpResponse(reply)

def disarm_bomb(request, arguments):
    arguments = str(arguments)
    arguments = arguments.split("&")
    reply = u"The bomb at %s:%s in the map \"%s\" is being disarmed." % (arguments[0], arguments[1], arguments[2])
    return HttpResponse(reply)
