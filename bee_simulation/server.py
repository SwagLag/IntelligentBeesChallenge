from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter
from bee_simulation.agents import Bee, Nectar, Hive
from bee_simulation.model import BeeSimulation

# Green
BEE_COLOR = "#000000"
NECTAR_COLOR = "#FFA500"
HIVE_COLOR = "#964B00"


def agent_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    # update portrayal characteristics for each object
    if isinstance(agent, Bee):
        portrayal["Shape"] = "circle"
        portrayal["r"] = 0.5
        portrayal["Layer"] = 2
        portrayal["Filled"] = "true"

        if agent.has_nectar:
            portrayal["Color"] = "Black"
        else:
            portrayal["Color"] = "Gray"

    if isinstance(agent, Nectar):
        portrayal["Shape"] = "circle"
        portrayal["r"] = 0.3
        portrayal["Layer"] = 0
        portrayal["Filled"] = "true"
        portrayal["Color"] = NECTAR_COLOR

    if isinstance(agent, Hive):
        portrayal["Shape"] = "rect"
        portrayal["w"] = 0.5
        portrayal['h'] = 0.5
        portrayal["Layer"] = 1
        portrayal["Filled"] = "true"
        portrayal["Color"] = HIVE_COLOR

    return portrayal


# dictionary of user settable parameters - these map to the model __init__ parameters
model_params = {
    "init_people": UserSettableParameter(
        "slider", "People", 3, 1, 10, description="Initial Number of Bees"
    ),
    "init_nectar": UserSettableParameter(
        "slider", "Nectar", 10, 1, 30, description="Initial Number of Nectar"
    ),
}

# set the portrayal function and size of the canvas for visualization
canvas_element = CanvasGrid(agent_portrayal, 6, 6, 500, 500)

# map data to chart in the ChartModule
chart_element = ChartModule(
    [
        {"Label": "Nectar Collected", "Color": NECTAR_COLOR},
    ]
)

# create instance of Mesa ModularServer
server = ModularServer(
    BeeSimulation,
    [canvas_element, chart_element],
    "Dance of the Bees",
    model_params=model_params,
)
