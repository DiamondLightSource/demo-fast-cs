from fastcs.backends import AsyncioBackend, EpicsBackend
from fastcs.mapping import Mapping

from demo_fast_cs.controllers import (
    IPConnectionSettings,
    TempController,
    TempControllerSettings,
)


def get_controller() -> TempController:
    ip_settings = IPConnectionSettings()
    settings = TempControllerSettings(4, ip_settings)
    tcont = TempController(settings)
    return tcont


async def run_controller() -> None:
    tcont = get_controller()
    await tcont.connect()
    print(f"Initial ramp rate: {tcont.ramp_rate.get()}")
    # await tcont.update()
    print(f"Starting ramp rate: {tcont.ramp_rate.get()}")
    # await tcont.put_ramp_rate(5)
    # await tcont.update()
    print(f"Final ramp rate: {tcont.ramp_rate.get()}")
    # trc = tcont.get_sub_controllers()[0]
    # await trc.update()
    # await tcont.update()
    # await asyncio.sleep(1)
    # await tcont.set_enabled(1)
    # await asyncio.sleep(3)
    # await tcont.update()
    # await asyncio.sleep(3)
    # await tcont.update()
    # await tcont.set_enabled(0)
    # await tcont.update()
    # await tcont.close()


def test_mapping() -> None:
    tcont = get_controller()
    m = Mapping(tcont)

    print(str(m))


def create_docs() -> None:
    tcont = get_controller()
    m = Mapping(tcont)
    backend = EpicsBackend(m)
    backend.create_docs()


def create_gui() -> None:
    tcont = get_controller()
    m = Mapping(tcont)
    backend = EpicsBackend(m)
    backend.create_gui()


def test_ioc() -> None:
    tcont = get_controller()
    m = Mapping(tcont)
    backend = EpicsBackend(m)
    ioc = backend.get_ioc()

    ioc.run()


def test_asyncio_backend() -> None:
    tcont = get_controller()
    m = Mapping(tcont)
    backend = AsyncioBackend(m)
    backend.run_interactive_session()


def main() -> None:
    # asyncio.run(test_ip_conn())
    # test_asyncio_backend()
    create_gui()
    test_ioc()


if __name__ == "__main__":
    main()
