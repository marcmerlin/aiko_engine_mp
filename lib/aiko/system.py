# lib/aiko/system.py: version: 2021-01-22 18:00 v05
#
# To Do
# ~~~~~
# - None, yet !

import gc

import aiko.event as event

import configuration.system

def gc_event():
  gc.collect()
  print("### GC:", gc.mem_free(), gc.mem_alloc())

def system_features_handler(pin_numbers):
  print("System special features")

def initialise(settings=configuration.system.settings):
  if configuration.main.parameter("gc_enabled", settings):
    event.add_timer_handler(gc_event, 60000)

  system_pins = configuration.main.parameter("system_pins", settings)
  if system_pins:
    import aiko.button
    aiko.button.initialise()
    aiko.button.add_multibutton_handler(system_features_handler, system_pins)
