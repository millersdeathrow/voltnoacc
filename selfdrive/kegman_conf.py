import json
import os


class KegmanConf:
  def __init__(self, CP=None):
    self.conf = self.read_config()
    if CP is not None:
      self.init_config(CP)

  def init_config(self, CP):
    if self.conf['tuneGernby'] != "1":
      self.conf['tuneGernby'] = str(1)

    # only fetch Kp, Ki, Kf sR and sRC from interface.py if it's a PID controlled car
    if CP.lateralTuning.which() == 'pid':
      if self.conf['Kp'] == "-1":
        self.conf['Kp'] = str(round(CP.lateralTuning.pid.kpV[0], 3))
      if self.conf['Ki'] == "-1":
        self.conf['Ki'] = str(round(CP.lateralTuning.pid.kiV[0], 3))
      if self.conf['Kf'] == "-1":
        self.conf['Kf'] = str('{:f}'.format(CP.lateralTuning.pid.kf))

    if self.conf['steerRatio'] == "-1":
      self.conf['steerRatio'] = str(round(CP.steerRatio, 3))

    if self.conf['steerRateCost'] == "-1":
      self.conf['steerRateCost'] = str(round(CP.steerRateCost, 3))

    if self.conf['steerActuatorDelay'] == "-1":
      self.conf['steerActuatorDelay'] = str(round(CP.steerActuatorDelay, 3))

    self.write_config(self.conf)

  def read_config(self):
    config = {
      "Kp": "-1",
      "Ki": "-1",
      "Kf": "-1",
      "steerRatio": "-1",
      "steerRateCost": "-1",
      "steerActuatorDelay": "-1",
      "deadzone": "0.0",
      "cameraOffset": "0.06",
      "wheelTouchSeconds": "180",
      "tuneGernby": "1",
      "slowOnCurves": "0",
      "lastTrMode": "1",
      "battChargeMin": "60",
      "battChargeMax": "70",
      "battPercOff": "25",
      "carVoltageMinEonShutdown": "11800",
      "brakeStoppingTarget": "0.25",
      "liveParams": "1",
      "leadDistance": "5",
      "1barBP0": "-0.1",
      "1barBP1": "2.25",
      "2barBP0": "-0.1",
      "2barBP1": "2.5",
      "3barBP0": "0.0",
      "3barBP1": "3.0",
      "1barMax": "2.1",
      "2barMax": "2.1",
      "3barMax": "2.1",
      "1barHwy": "0.4",
      "2barHwy": "0.3",
      "3barHwy": "0.1",
      "sR_boost": "0",
      "sR_BP0": "0",
      "sR_BP1": "0",
      "sR_time": "1",
      "ALCnudgeLess": "0",
      "ALCminSpeed": "20.1168",
      "ALCtimer": "2.0",
      "CruiseDelta": "8",
      "CruiseEnableMin": "40"
    }

    if os.path.isfile('/data/kegman.json'):
      with open('/data/kegman.json', 'r') as f:
        read_config = json.load(f)

      if "tuneGernby" in read_config:
        config["tuneGernby"] = read_config["tuneGernby"]
        config["Kp"] = read_config["Kp"]
        config["Ki"] = read_config["Ki"]

      if "Kf" in read_config:
        config["Kf"] = read_config["Kf"]

      if "steerRatio" in read_config:
        config["steerRatio"] = read_config["steerRatio"]

      if "steerRateCost" in read_config:
        config["steerRateCost"] = read_config["steerRateCost"]

      if "steerActuatorDelay" in read_config:
        config["steerActuatorDelay"] = read_config["steerActuatorDelay"]

      if "deadzone" in read_config:
        config["deadzone"] = read_config["deadzone"]

      if "cameraOffset" in read_config:
        config["cameraOffset"] = read_config["cameraOffset"]

      if "wheelTouchSeconds" in read_config:
        config["wheelTouchSeconds"] = read_config["wheelTouchSeconds"]

      if "slowOnCurves" in read_config:
        config["slowOnCurves"] = read_config["slowOnCurves"]

      if "battPercOff" in read_config:
        config["battPercOff"] = read_config["battPercOff"]
        config["carVoltageMinEonShutdown"] = read_config["carVoltageMinEonShutdown"]
        config["brakeStoppingTarget"] = read_config["brakeStoppingTarget"]

      if "liveParams" in read_config:
        config["liveParams"] = read_config["liveParams"]

      if "leadDistance" in read_config:
        config["leadDistance"] = read_config["leadDistance"]

      if "1barBP0" in read_config:
        config["1barBP0"] = read_config["1barBP0"]
        config["1barBP1"] = read_config["1barBP1"]
        config["2barBP0"] = read_config["2barBP0"]
        config["2barBP1"] = read_config["2barBP1"]
        config["3barBP0"] = read_config["3barBP0"]
        config["3barBP1"] = read_config["3barBP1"]

      if "1barMax" in read_config:
        config["1barMax"] = read_config["1barMax"]
        config["2barMax"] = read_config["2barMax"]
        config["3barMax"] = read_config["3barMax"]

      if "1barHwy" in read_config:
        config["1barHwy"] = read_config["1barHwy"]
        config["2barHwy"] = read_config["2barHwy"]
        config["3barHwy"] = read_config["3barHwy"]

      if "sR_boost" in read_config:
        config["sR_boost"] = read_config["sR_boost"]
        config["sR_BP0"] = read_config["sR_BP0"]
        config["sR_BP1"] = read_config["sR_BP1"]
        config["sR_time"] = read_config["sR_time"]

      if "ALCnudgeLess" in read_config:
        config["ALCnudgeLess"] = read_config["ALCnudgeLess"]
        config["ALCminSpeed"] = read_config["ALCnudgeLess"]

      if "ALCtimer" in read_config:
        config["ALCtimer"] = read_config["ALCtimer"]

      if "CruiseDelta" in read_config:
        config["CruiseDelta"] = read_config["CruiseDelta"]

      if "CruiseEnableMin" in read_config:
        config["CruiseEnableMin"] = read_config["CruiseEnableMin"]

    self.write_config(config)
    return config

  def write_config(self, config):
    if not os.path.exists('/data'):
      os.mkdir('/data')

    with open('/data/kegman.json', 'w') as f:
      json.dump(config, f, indent=2, sort_keys=True)
      os.chmod("/data/kegman.json", 0o764)

    print("updated kegman.json")
