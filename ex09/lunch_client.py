#!/usr/bin/env python3

from pydbus import SessionBus

bus = SessionBus()
lunch_service = bus.get("net.c0ff33.LunchService")

lunch_service.add("kebs", "zenek", "na grubym")
lunch_service.add("makaron", "franek", "z sosem pomidorowym")
lunch_service.dump()

