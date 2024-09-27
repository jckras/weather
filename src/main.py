import asyncio
import sys

from viam.module.module import Module
from viam.components.sensor import Sensor
from .meteo_PM import meteo_PM


from viam.resource.registry import Registry, ResourceCreatorRegistration


async def main():
    """This function creates and starts a new module, after adding all desired resources.
    Resources must be pre-registered. For an example, see the `__init__.py` file.
    """

    Registry.register_resource_creator(Sensor.SUBTYPE, meteo_PM.MODEL, ResourceCreatorRegistration(meteo_PM.new, meteo_PM.validate))

    module = Module.from_args()
    module.add_model_from_registry(Sensor.SUBTYPE, meteo_PM.MODEL)
    await module.start()

if __name__ == "__main__":
    asyncio.run(main())
