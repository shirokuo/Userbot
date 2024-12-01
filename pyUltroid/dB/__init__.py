from .. import run_as_module
import resources
if not run_as_module:
    from ..exceptions import RunningAsFunctionLibError

    raise RunningAsFunctionLibError(
        "You are running 'pyUltroid' as a functions lib, not as run module. You can't access this folder.."
    )

from .. import *

DEVLIST = [
    719195224,  # @xditya
    1322549723,  # @danish_00
    1903729401,  # @its_buddhhu
    1303895686,  # @Sipak_OP
    611816596,  # @Arnab431
    1318486004,  # @sppidy
    803243487,  # @hellboi_atul
]

ULTROID_IMAGES = [
    f"https://graph.org/file/{_}.jpg"
    for _ in [
       "ec250c66268b62ee4ade6",
        "3c25230ae30d246194eba",
        "b01715a61b9e876c0d45d",
        "4ceaf720a96a24527ecff",
        "a96223b574f29f3f0d184",
        "6e081d339a01cc6190393",
    ]
]

ALIVE_TEXT = [
    "Jangan minum dan mengetik.",
    "Saya pikir Anda harus pulang atau lebih baik ke rumah sakit jiwa.",
    "Perintah tidak ditemukan. Sama seperti otak Anda.",
    "Apakah kamu sadar bahwa kamu membodohi dirimu sendiri? Ternyata tidak.",
    "Anda bisa mengetik lebih baik dari itu.",
    "Bot aturan 544 bagian 9 mencegah saya membalas orang bodoh seperti Anda.",
    "Maaf, kami tidak menjual otak.",
    "Percayalah kamu tidak normal.",
    "Saya yakin otak Anda terasa seperti baru, mengingat Anda tidak pernah menggunakannya.",
    "Jika saya ingin bunuh diri, saya akan meningkatkan ego Anda dan melompat ke IQ Anda.",
    "Zombie memakan otak ... kamu aman.",
    "Anda tidak berevolusi dari kera, mereka berevolusi dari Anda.",
    "Kembalilah dan bicara padaku ketika IQ mu melebihi umurmu.",
    "Saya tidak mengatakan Anda bodoh, saya hanya mengatakan bahwa Anda tidak beruntung dalam hal berpikir.",
    "Kamu berbicara bahasa apa? Karena terdengar seperti omong kosong.",
    "Kebodohan bukanlah kejahatan jadi kamu bebas pergi.",
    "Anda adalah bukti bahwa evolusi BISA mundur.",
    "Aku akan bertanya berapa umurmu tapi aku tahu kamu tidak bisa menghitung setinggi itu.",
    "Sebagai orang luar, apa pendapat Anda tentang umat manusia?",
    "Otak bukanlah segalanya. Dalam kasusmu mereka bukan apa-apa.",
    "Biasanya orang hidup dan belajar. Kamu hidup saja.",
    "Aku tidak tahu apa yang membuatmu begitu bodoh, tapi itu benar-benar berhasil.",
    "Teruslah berbicara, suatu hari nanti kamu akan mengatakan sesuatu yang cerdas! (Meskipun aku ragu)"
    "Shock saya, katakan sesuatu yang cerdas.",
    "IQ Anda lebih rendah dari ukuran sepatu Anda.",
    "Aduh! Neurotransmiter Anda tidak lagi bekerja.",
    "Apakah kamu gila kamu bodoh.",
    "Setiap orang berhak untuk menjadi bodoh tetapi Anda menyalahgunakan hak istimewa tersebut.",
    "Maaf aku menyakiti perasaanmu saat menyebutmu bodoh. Kupikir kamu sudah tahu itu.",
    "Anda harus mencoba mencicipi sianida.",
    "Enzim Anda dimaksudkan untuk mencerna racun tikus.",
    "Kamu harus mencoba tidur selamanya.",
    "Ambil pistol dan tembak dirimu sendiri.",
    "Anda bisa membuat rekor dunia dengan melompat dari pesawat tanpa parasut.",
    "Berhenti berbicara BS dan melompat di depan kereta peluru yang sedang berjalan.",
    "Cobalah mandi dengan Hydrochloric Acid daripada air.",
    "Coba ini: jika Anda menahan napas di bawah air selama satu jam, Anda dapat menahannya selamanya.",
    "Go Green! Berhenti menghirup Oksigen.",
    "Tuhan sedang mencarimu. Kamu harus pergi untuk bertemu dengannya.",
    "berikan 100% mu. Sekarang, pergi donor darah.",
    "Cobalah melompat dari gedung seratus lantai tetapi Anda hanya dapat melakukannya sekali.",
    "Anda harus menyumbangkan otak Anda melihat bahwa Anda tidak pernah menggunakannya.",
    "Relawan untuk target dalam jarak tembak.",
    "Tembak kepala itu menyenangkan. Dapatkan dirimu sendiri.",
    "Anda harus mencoba berenang dengan hiu putih besar.",
    "Anda harus mengecat diri Anda dengan warna merah dan berlari dalam bull marathon.",
    "Anda bisa tetap di bawah air selama sisa hidup Anda tanpa harus kembali lagi.",
    "Bagaimana kalau kamu berhenti bernapas selama 1 hari? Itu akan bagus.",
    "Cobalah memprovokasi harimau saat kalian berdua berada di dalam sangkar.",
    "Sudahkah Anda mencoba menembak diri Anda sendiri setinggi 100m menggunakan kanon.",
    "Anda harus mencoba menahan TNT di mulut Anda dan menyalakannya.",
    "Cobalah bermain menangkap dan melempar dengan RDX itu menyenangkan.",
    "Saya dengar phogine beracun tapi saya rasa Anda tidak keberatan menghirupnya untuk bersenang-senang.",
    "Luncurkan diri Anda ke luar angkasa sambil melupakan oksigen di Bumi.",
    "Kamu harus mencoba bermain ular tangga, dengan ular sungguhan dan tanpa tangga.",
    "Menari telanjang di beberapa kabel HT.",
    "Gunung Berapi Aktif adalah kolam renang terbaik untuk Anda.",
    "Anda harus mencoba mandi air panas di gunung berapi.",
    "Cobalah untuk menghabiskan satu hari di peti mati dan itu akan menjadi milikmu selamanya.",
    "Pukul Uranium dengan neutron yang bergerak lambat di hadapanmu. Ini akan menjadi pengalaman yang berharga.",
    "Anda bisa menjadi orang pertama yang menginjak matahari. Selamat mencoba.",
]
PING_IMAGES = [f"/resources/extras/ping_pic.mp4"]

stickers = [
    "CAADAQADeAIAAm_BZBQh8owdViocCAI",
    "CAADAQADegIAAm_BZBQ6j8GpKtnrSgI",
    "CAADAQADfAIAAm_BZBQpqC84n9JNXgI",
    "CAADAQADfgIAAm_BZBSxLmTyuHvlzgI",
    "CAADAQADgAIAAm_BZBQ3TZaueMkS-gI",
    "CAADAQADggIAAm_BZBTPcbJMorVVsQI",
    "CAADAQADhAIAAm_BZBR3lnMZRdsYxAI",
    "CAADAQADhgIAAm_BZBQGQRx4iaM4pQI",
    "CAADAQADiAIAAm_BZBRRF-cjJi_QywI",
    "CAADAQADigIAAm_BZBQQJwfzkqLM0wI",
    "CAADAQADjAIAAm_BZBQSl5GSAT0viwI",
    "CAADAQADjgIAAm_BZBQ2xU688gfHhQI",
    "CAADAQADkAIAAm_BZBRGuPNgVvkoHQI",
    "CAADAQADpgIAAm_BZBQAAZr0SJ5EKtQC",
    "CAADAQADkgIAAm_BZBTvuxuayqvjhgI",
    "CAADAQADlAIAAm_BZBSMZdWN2Yew1AI",
    "CAADAQADlQIAAm_BZBRXyadiwWGNkwI",
    "CAADAQADmAIAAm_BZBQDoB15A1jS1AI",
    "CAADAQADmgIAAm_BZBTnOLQ8_d72vgI",
    "CAADAQADmwIAAm_BZBTve1kgdG0Y5gI",
    "CAADAQADnAIAAm_BZBQUMyFiylJSqQI",
    "CAADAQADnQIAAm_BZBSMAe2V4pwhNgI",
    "CAADAQADngIAAm_BZBQ06D92QL_vywI",
    "CAADAQADnwIAAm_BZBRw7UAbr6vtEgI",
    "CAADAQADoAIAAm_BZBRkv9DnGPXh_wI",
    "CAADAQADoQIAAm_BZBQwI2NgQdyKlwI",
    "CAADAQADogIAAm_BZBRPHJF3XChVLgI",
    "CAADAQADowIAAm_BZBThpas7rZD6DAI",
    "CAADAQADpAIAAm_BZBQcC2DpZcCw1wI",
    "CAADAQADpQIAAm_BZBQKruTcEU4ntwI",
]
