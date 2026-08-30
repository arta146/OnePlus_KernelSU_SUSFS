# OP13R performance feature patches

These patches target the OnePlus Android 14 Linux 6.1 common kernel selected by
`manifests/a15/oneplus_13r_v.xml` at source revision
`7b9a23054ab0ada2886ed34a2137b9d0312891ff`.

## BORE

`0001-sched-bore-5.3.0-android14-6.1.patch` integrates the BORE 5.3.0 scheduler
logic for the classic CFS implementation used by this Android kernel. Scheduler
state is stored in the existing Android KABI reserves of `struct sched_entity`.
BORE is enabled by `CONFIG_SCHED_BORE=y` and remains configurable through its
`kernel.sched_*` sysctls.

Upstream: <https://github.com/firelzrd/bore-scheduler>

Android 6.1 port reference:
<https://github.com/Mohithash/kernel_xiaomi_sm8635/tree/peridot-6.1.175>

## LZ4KD

`0002-lz4kd-zram-android14-6.1.patch` connects LZ4KD to the kernel compression
API and ZRAM. The implementation files are fetched from `SukiSU_patch` at the
pinned commit `547ae94bcaec53d030398f857950c64662043a5d`; unrelated upstream module
blacklist changes are deliberately not included.

The OP13R configuration enables `CONFIG_CRYPTO_LZ4KD=y` and selects LZ4KD as
the default ZRAM compressor.

Upstream: <https://github.com/SukiSU-Ultra/SukiSU_patch>
