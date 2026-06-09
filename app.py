import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 8", layout="centered")

# --- DATABASE SOAL LOKAL LENGKAP & BERSIH (BAB 8) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # --- Pola 1: 〜はずがない ・ 〜わけがない ---
        {
            "id": 1, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin...)",
            "kanji": "ちゃんと約束したから彼は来ないはずがないが、どうしたのかなあ。",
            "hiragana": "ちゃんと やくそく した から かれ は こない はず が ない が 、 どうした のかなあ 。",
            "arti": "Karena sudah berjanji dengan jelas, tidak mungkin dia tidak datang. Tapi, ada apa ya (kenapa belum datang)?",
            "kunci": ["ちゃんと", "約束", "した", "から", "彼", "は", "来ない", "はず", "が", "ない", "が", "、", "どうした", "のかなあ", "。"],
            "soal": ["約束", "ちゃんと", "はず", "ない", "だ", "から", "彼", "は", "来ない", "が", "と", "した", "ん", "のかなあ", "どうした", "。"]
        },
        {
            "id": 2, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin...)",
            "kanji": "今日あの店が休みのはずはありません。電話で確認したんですから。",
            "hiragana": "きょう あの みせ が やすみ の はず は ありません 。 でんわ で かくにん した ん です から 。",
            "arti": "Tidak mungkin toko itu libur hari ini. Karena saya sudah memastikannya lewat telepon.",
            "kunci": ["今日", "あの", "店", "が", "休み", "の", "はず", "は", "ありません", "。", "電話", "で", "確認", "した", "ん", "です", "から", "。"],
            "soal": ["今日", "休み", "あの", "店", "が", "はず", "は", "ありません", "電話", "微調整", "確認", "した", "ん", "です", "から", "の", "。", "。"]
        },
        {
            "id": 3, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin...)",
            "kanji": "国家試験だから易しいはずがない。がんばらなくてはな。",
            "hiragana": "こっかしけん だから やさしい はず が ない 。 がんばらなくては な 。",
            "arti": "Karena ini ujian nasional, tidak mungkin mudah. Harus berjuang, ya.",
            "kunci": ["国家", "試験", "だ", "から", "易しい", "はず", "が", "ない", "。", "がんばらなくては", "な", "。"],
            "soal": ["国家", "試験", "だ", "から", "易しい", "はず", "が", "ない", "がんばらなくては", "の", "な", "。", "……"]
        },
        {
            "id": 4, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin...)",
            "kanji": "こんなに大きいお菓子、わたしに貰えるわけがないでしょう。",
            "hiragana": "こんなに おおきい おかし 、 わたし に もらえる わけ が ない でしょう 。",
            "arti": "Kue yang sebesar ini, tidak mungkin bisa saya dapatkan/terima, kan?",
            "kunci": ["こんなに", "大きい", "お菓子", "、", "わたし", "に", "貰える", "わけ", "が", "ない", "でしょう", "。"],
            "soal": ["こんなに", "大きい", "お菓子", "わたし", "に", "貰える", "わけ", "が", "ない", "でしょう", "。"]
        },
        {
            "id": 5, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin...)",
            "kanji": "試合に勝つために練習しているのだから、練習が厳しいわけがない。",
            "hiragana": "しあい に かつ ため に れんしゅう して いる の だ から 、 れんしゅう が きびしい わけ が ない 。",
            "arti": "Karena berlatih demi memenangkan pertandingan, tidak mungkin latihannya tidak keras/ketat.",
            "kunci": ["試合", "に", "勝つ", "ため", "に", "練習", "して", "いる", "の", "だ", "から", "、", "練習", "が", "厳しい", "わけ", "が", "ない", "。"],
            "soal": ["試合", "に", "勝つ", "ため", "に", "練習", "して", "いる", "の", "だ", "から", "練習", "が", "厳しい", "わけ", "が", "ない", "しない", "。"]
        },
        # --- Pola 2: 〜とは限らない ---
        {
            "id": 6, 
            "pola": "Pola 2: 〜とは限らない (Belum tentu... / Tidak selalu...)",
            "kanji": "この歌は古くから歌われているが、日本人がみんな知っているとは限らない。",
            "hiragana": "この うた は ふるく から うたわれている が 、 にほんじん が みんな しっている と は かぎらない 。",
            "arti": "Lagu ini dinyanyikan sejak dulu, tetapi belum tentu semua orang Jepang tahu.",
            "kunci": ["この", "歌", "は", "古く", "から", "歌われて", "いる", "が", "、", "日本人", "が", "みんな", "知って", "いる", "と", "は", "限らない", "。"],
            "soal": ["この", "歌", "は", "古く", "から", "歌われて", "いる", "が", "日本人", "が", "みんな", "知って", "いる", "と", "は", "限らない", "。"]
        },
        {
            "id": 7, 
            "pola": "Pola 2: 〜とは限らない (Belum tentu... / Tidak selalu...)",
            "kanji": "値段が高い物が必ずしもいいとは限らない。",
            "hiragana": "ねだん が たかい もの が かならずしも いい と は かぎらない 。",
            "arti": "Barang yang harganya mahal itu tidak selalu (belum tentu) bagus.",
            "kunci": ["値段", "が", "高い", "物", "が", "必ずしも", "いい", "と", "は", "限らない", "。"],
            "soal": ["値段", "が", "高い", "物", "が", "必ずしも", "いい", "と", "は", "限らない", "。"]
        },
        {
            "id": 8, 
            "pola": "Pola 2: 〜とは限らない (Belum tentu... / Tidak selalu...)",
            "kanji": "旅行中にけがをしないとは限りません。保険に入っておいたほうがいいですよ。",
            "hiragana": "りょこうちゅう に けが を しない と は かぎりません 。 ほけん に はいって おいた ほう が いい です よ 。",
            "arti": "Bukan berarti (belum tentu) tidak akan terluka selama perjalanan. Lebih baik masuk asuransi dulu, lho.",
            "kunci": ["旅行", "中", "に", "けが", "を", "しない", "と", "は", "限りません", "。", "保険", "に", "入って", "おいた", "ほう", "が", "いい", "です", "よ", "。"],
            "soal": ["旅行", "中", "に", "けが", "を", "しない", "と", "は", "限りません", "保険", "に", "入って", "おいた", "ほう", "が", "いい", "です", "よ", "。"]
        },
        {
            "id": 9, 
            "pola": "Pola 2: 〜とは限らない (Belum tentu... / Tidak selalu...)",
            "kanji": "新聞に書いてあることがいつも本当のことだとは限らない。",
            "hiragana": "しんぶん に かいて ある こと が いつも ほんとう の こと だ と は かぎらない 。",
            "arti": "Apa yang tertulis di koran tidak selalu (belum tentu) merupakan hal yang benar.",
            "kunci": ["新聞", "に", "書いて", "ある", "こと", "が", "いつも", "本当", "の", "こと", "だ", "と", "は", "限らない", "。"],
            "soal": ["新聞", "に", "書いて", "ある", "こと", "が", "いつも", "本当", "の", "こと", "だ", "と", "は", "限らない", "。"]
        },
        # --- Pola 3: 〜わけではない ・ 〜というわけではない ・ 〜のではない ---
        {
            "id": 10, 
            "pola": "Pola 3: 〜わけではない (Bukan berarti... / Tidak selalu...)",
            "kanji": "長い間本をお借りしたままでしたが、忘れていたわけではありません。",
            "hiragana": "ながい あいだ ほん を おかり した まま でした が 、 わすれていた わけ で は ありません 。",
            "arti": "Saya telah meminjam buku dalam waktu lama, tetapi bukan berarti saya melupakannya.",
            "kunci": ["長い", "間", "本", "を", "お借り", "した", "まま", "でした", "が", "、", "忘れて", "いた", "わけ", "で", "は", "ありません", "。"],
            "soal": ["長い", "間", "本", "を", "お借り", "した", "まま", "でした", "が", "忘れて", "いた", "わけ", "で", "は", "ありません", "。"]
        },
        {
            "id": 11, 
            "pola": "Pola 3: 〜わけではない (Bukan berarti... / Tidak selalu...)",
            "kanji": "いつでも電話に出られるわけではありません。連絡はメールでお願いします。",
            "hiragana": "いつでも でんわ に でられる わけ で は ありません 。 れんらく は メール で おねがい します 。",
            "arti": "Bukan berarti saya bisa mengangkat telepon kapan saja. Untuk hubungi mohon via email saja.",
            "kunci": ["いつでも", "電話", "に", "出られる", "わけ", "で", "は", "ありません", "。", "連絡", "は", "メール", "で", "お願い", "します", "。"],
            "soal": ["いつでも", "電話", "に", "出られる", "わけ", "で", "は", "ありません", "連絡", "は", "メール", "で", "お願い", "します", "。"]
        },
        {
            "id": 12, 
            "pola": "Pola 3: 〜というわけではない (Bukan berarti [secara khusus]...)",
            "kanji": "この仕事が好きだというわけではないが、彼と一緒に仕事ができて楽しい。",
            "hiragana": "この しごと が すき だ という わけ で は ない が 、 かれ と いっしょ に しごと が できて たのしい 。",
            "arti": "Bukan berarti saya menyukai pekerjaan ini, tetapi saya senang bisa bekerja bersama dia.",
            "kunci": ["この", "仕事", "が", "好き", "だ", "という", "わけ", "で", "は", "ない", "が", "、", "彼", "と", "一緒", "に", "仕事", "が", "できて", "楽しい", "。"],
            "soal": ["この", "仕事", "が", "好き", "だ", "という", "わけ", "で", "は", "ない", "が", "彼", "と", "一緒", "に", "仕事", "が", "できて", "楽しい", "。"]
        },
        {
            "id": 13, 
            "pola": "Pola 3: 〜のではない (Bukan... [Melainkan...])",
            "kanji": "転勤するのではありません。会社を辞めるんです。",
            "hiragana": "てんきん する の で は ありません 。 かいしゃ を やめる ん です 。",
            "arti": "Bukan pindah tugas (cabang). Saya berhenti dari perusahaan.",
            "kunci": ["転勤", "する", "の", "で", "は", "ありません", "。", "会社", "を", "辞める", "ん", "です", "。"],
            "soal": ["転勤", "する", "の", "で", "は", "ありません", "会社", "を", "辞める", "ん", "です", "。", "。"]
        },
        {
            "id": 14, 
            "pola": "Pola 3: 〜のではない (Bukan... [Melainkan...])",
            "kanji": "Ａ「いい帽子ね。良かったでしょう。」Ｂ「これは買ったんじゃないの。自分で作ったの。」",
            "hiragana": "Ａ「 いい ぼうし ね 。 よかった でしょう 。」 Ｂ「 これ は かった ん じゃない の 。 じぶん で つくった の 。」",
            "arti": "A: \"Topi yang bagus ya. Pasti mahal/bagus kan.\" B: \"Ini bukan beli, lho. Bikin sendiri.\"",
            "kunci": ["Ａ「いい", "帽子", "ね", "。", "良かった", "desktop", "。」", "Ｂ「これ", "は", "買った", "ん", "じゃない", "の", "、", "自分で", "作った", "の", "。」"],
            "soal": ["Ａ「いい", "帽子", "ね", "良かった", "でしょう", "。」", "Ｂ「これ", "は", "買った", "ん", "じゃない", "の", "自分で", "作った", "の", "。」"]
        },
        # --- Pola 4: 〜ないことはない ---
        {
            "id": 15, 
            "pola": "Pola 4: 〜ないことはない (Bukan berarti tidak... / Bisa saja...)",
            "kanji": "ここから駅まで歩けないことはありませんが、かなり時間がかかりますよ。",
            "hiragana": "ここ から えき まで あるけない こと は ありません が 、 かなり じかん が かかります よ 。",
            "arti": "Bukan berarti tidak bisa berjalan dari sini ke stasiun, tapi memakan waktu yang cukup lama, lho.",
            "kunci": ["ここ", "から", "駅", "まで", "歩けない", "こと", "は", "ありません", "が", "、", "かなり", "時間", "が", "かかります", "よ", "。"],
            "soal": ["ここ", "から", "駅", "まで", "歩けない", "こと", "は", "ありません", "が", "かなり", "時間", "が", "かかります", "よ", "。"]
        },
        {
            "id": 16, 
            "pola": "Pola 4: 〜ないことはない (Bukan berarti tidak... / Bisa saja...)",
            "kanji": "この店のカレーもおいしくないことはないが、わたしはもっと辛いのが好きだ。",
            "hiragana": "この みせ の カレー も おいしくない こと は ない が 、 わたし は もっと からい の が すき だ 。",
            "arti": "Kari toko ini juga bukan berarti tidak enak, tapi saya lebih suka yang lebih pedas.",
            "kunci": ["この", "店", "の", "カレー", "も", "おいしくない", "こと", "は", "ない", "が", "、", "わたし", "は", "もっと", "辛い", "の", "が", "好き", "だ", "。"],
            "soal": ["この", "店", "の", "カレー", "も", "おいしくない", "こと", "は", "ない", "が", "わたし", "は", "もっと", "辛い", "の", "が", "好き", "だ", "。"]
        },
        {
            "id": 17, 
            "pola": "Pola 4: 〜ないことはない (Bukan berarti tidak... / Bisa saja...)",
            "kanji": "試験の結果が心配でないことはないのですが、今は終わってほっとしています。",
            "hiragana": "しけん の けっか が しんぱい で ない こと は ない の です が 、 いま は おわって ほっと して います 。",
            "arti": "Bukan berarti saya tidak khawatir dengan hasil ujiannya, tapi sekarang saya lega karena sudah selesai.",
            "kunci": ["試験", "の", "結果", "が", "心配", "で", "ない", "こと", "は", "ない", "の", "です", "が", "、", "今", "は", "終わって", "ほっと", "して", "います", "。"],
            "soal": ["試験", "の", "結果", "が", "心配", "で", "ない", "こと", "は", "ない", "の", "です", "が", "今", "は", "終わって", "ほっと", "して", "います", "。"]
        },
        # --- Pola 5: 〜ことは〜が、… ---
        {
            "id": 18, 
            "pola": "Pola 5: 〜ことは〜が、… (Memang... sih, tapi...)",
            "kanji": "彼からの手紙は読んだことは読んだんですが、意味がよくわかりませんでした。",
            "hiragana": "かれ から の てがみ は よんだ こと は よんだ ん です が 、 いみ が よく わかりませんでした 。",
            "arti": "Surat dari dia memang sudah saya baca sih, tapi saya tidak begitu mengerti artinya.",
            "kunci": ["彼", "から", "の", "手紙", "は", "読んだ", "こと", "は", "読んだ", "ん", "です", "が", "、", "意味", "が", "よく", "わかりませんでした", "。"],
            "soal": ["彼", "から", "の", "手紙", "は", "読んだ", "こと", "は", "読んだ", "ん", "です", "が", "意味", "が", "よく", "わかりませんでした", "。"]
        },
        {
            "id": 19, 
            "pola": "Pola 5: 〜ことは〜が、… (Memang... sih, tapi...)",
            "kanji": "わたしは泳げることは泳げますが、長い距離はだめなんです。",
            "hiragana": "わたし は およげる こと は およげます が 、 ながい きょり は だめ な ん です 。",
            "arti": "Saya memang bisa berenang sih, tapi kalau jarak jauh tidak bisa.",
            "kunci": ["わたし", "は", "泳げる", "こと", "は", "泳げます", "が", "、", "長い", "距離", "は", "だめ", "な", "ん", "です", "。"],
            "soal": ["わたし", "は", "泳げる", "こと", "は", "泳げます", "が", "長い", "距離", "は", "だめ", "な", "ん", "です", "。"]
        },
        {
            "id": 20, 
            "pola": "Pola 5: 〜ことは〜が、… (Memang... sih, tapi...)",
            "kanji": "この本は高いことは高いが、写真が多くて楽しめそうだ。",
            "hiragana": "この ほん は たかい こと は たかい が 、 しゃしん が おおくて たのしめ そう だ 。",
            "arti": "Buku ini memang mahal sih, tapi tampaknya menyenangkan karena banyak fotonya.",
            "kunci": ["この", "本", "は", "高い", "こと", "は", "高い", "が", "、", "写真", "が", "多くて", "楽しめ", "そう", "だ", "。"],
            "soal": ["この", "本", "は", "高い", "こと", "は", "高い", "が", "写真", "が", "多くて", "楽しめ", "そう", "だ", "。"]
        },
        {
            "id": 21, 
            "pola": "Pola 5: 〜ことは〜が、… (Memang... sih, tapi...)",
            "kanji": "子どもを育てるのは大変なことは大変だが、成長が楽しみで大変さを忘れる。",
            "hiragana": "こども を そだてる の は たいへん な こと は たいへん だ が 、 せいちょう が たのしみ で たいへん さ を わすれる 。",
            "arti": "Membesarkan anak memang melelahkan sih, tapi kelelahan itu terlupakan karena menantikan pertumbuhannya.",
            "kunci": ["子ども", "を", "育てる", "の", "は", "大変", "な", "こと", "は", "大変", "だ", "が", "、", "成長", "が", "楽しみ", "で", "大変さ", "を", "忘れる", "。"],
            "soal": ["子ども", "を", "育てる", "の", "は", "大変", "な", "こと", "は", "大変", "だ", "が", "成長", "が", "楽しみ", "で", "大変さ", "を", "忘れる", "。"]
        }
    ]

# --- INISIALISASI STATE ---
if "index_soal" not in st.session_state:
    st.session_state.index_soal = 0
if "jawaban_user" not in st.session_state:
    st.session_state.jawaban_user = []
if "bank_kata" not in st.session_state:
    st.session_state.bank_kata = []
if "status_periksa" not in st.session_state:
    st.session_state.status_periksa = False

if "idx_kata_dipilih" not in st.session_state:
    st.session_state.idx_kata_dipilih = None
if "mode_tukar" not in st.session_state:
    st.session_state.mode_tukar = False

soal_sekarang = st.session_state.database_soal[st.session_state.index_soal]

if not st.session_state.bank_kata and not st.session_state.jawaban_user:
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_sekarang["soal"])]

# --- STYLING CSS ---
st.markdown("""
<style>
    div[data-testid="stStatusWidget"] + div div[data-testid="stWidgetLabel"] {
        display: none;
    }
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 6px !important;
    }
    [data-testid="stHorizontalBlock"] > div {
        flex: 1 1 22% !important; 
        min-width: 70px !important; 
    }
    .info-box {
        background-color: #e8f4fd;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #1fa2ff;
        margin-bottom: 20px;
    }
    .text-bunpou { font-size: 1.05rem; font-weight: bold; color: #1fa2ff; margin: 0 0 6px 0; }
    .text-arti { font-size: 1.2rem; font-weight: bold; color: #1a1a1a; margin: 0; }
    
    div.stButton > button {
        border-radius: 12px !important;
        font-weight: bold !important;
        padding: 6px 10px !important;
    }
    .swap-indicator {
        background-color: #e6fffa;
        border: 1px dashed #319795;
        padding: 10px;
        border-radius: 8px;
        color: #234e52;
        font-weight: bold;
        margin-bottom: 10px;
        font-size: 0.9rem;
    }
    
    /* Style Bulat Navigasi Nomor Soal (1, 2, 3...) */
    .stButton > button[key^="lompat_"] {
        border-radius: 50% !important;
        width: 40px !important;
        height: 40px !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🦉 Bunpou Master (BAB 8)")
st.caption(f"Soal {soal_sekarang['id']} dari {len(st.session_state.database_soal)}")
st.markdown("---")

st.markdown(f"""
<div class="info-box">
    <p class="text-bunpou">📖 {soal_sekarang['pola']}</p>
    <p class="text-arti">🇮🇩 {soal_sekarang['arti']}</p>
</div>
""", unsafe_allow_html=True)

# --- MENU UTAMA INTERAKTIF (FRAGMENT) ---
@st.fragment
def render_kuis_lengkap():
    st.write("### Kalimat Susunanmu:")
    
    mode = st.radio(
        "Aksi Sentuhan Papan:",
        ["Copot Kata (Normal)", "Tukar Posisi 2 Kata 🔄"],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    if mode == "Tukar Posisi 2 Kata 🔄":
        st.session_state.mode_tukar = True
        if st.session_state.idx_kata_dipilih is not None:
            kata_terpilih = st.session_state.jawaban_user[st.session_state.idx_kata_dipilih]["teks"]
            st.markdown(f'<div class="swap-indicator">📍 Kata [{kata_terpilih}] terpilih. Sekarang klik kata tujuan!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="swap-indicator">💡 Klik kata pertama yang ingin ditukar posisinya...</div>', unsafe_allow_html=True)
    else:
        st.session_state.mode_tukar = False
        st.session_state.idx_kata_dipilih = None

    if not st.session_state.jawaban_user:
        st.markdown("<div style='border-bottom: 2px solid #e5e5e5; padding-bottom: 15px; margin-bottom: 20px; color:#aaaaaa; font-style:italic;'>Klik kata di bawah untuk mulai menyusun...</div>", unsafe_allow_html=True)
    else:
        opsi_papan = [f"{idx}. {item['teks']}" for idx, item in enumerate(st.session_state.jawaban_user)]
        format_papan = {opt: opt.split(". ", 1)[1] for opt in opsi_papan}
        
        klik_papan = st.pills(
            label="Papan Jawaban",
            options=opsi_papan,
            format_func=lambda x: format_papan[x],
            selection_mode="single",
            label_visibility="collapsed"
        )
        st.markdown("<div style='border-bottom: 2px solid #e5e5e5; margin-top: -10px; margin-bottom: 25px;'></div>", unsafe_allow_html=True)
        
        if klik_papan:
            idx_klik = int(klik_papan.split(". ")[0])
            
            if st.session_state.mode_tukar:
                if st.session_state.idx_kata_dipilih is None:
                    st.session_state.idx_kata_dipilih = idx_klik
                    st.rerun()
                else:
                    idx1 = st.session_state.idx_kata_dipilih
                    idx2 = idx_klik
                    if idx1 != idx2:
                        st.session_state.jawaban_user[idx1], st.session_state.jawaban_user[idx2] = st.session_state.jawaban_user[idx2], st.session_state.jawaban_user[idx1]
                    st.session_state.idx_kata_dipilih = None
                    st.rerun()
            else:
                kata_dicopot = st.session_state.jawaban_user.pop(idx_klik)
                for kata_bank in st.session_state.bank_kata:
                    if kata_bank["id"] == kata_dicopot["id"]:
                        kata_bank["dipakai"] = False
                st.rerun()

    st.write("### Pilihan Kata:")
    cols_pilihan = st.columns(4)
    for idx, item in enumerate(st.session_state.bank_kata):
        posisi_kolom = idx % 4
        with cols_pilihan[posisi_kolom]:
            if item["dipakai"]:
                st.button(" ", key=f"disabled_{item['id']}", disabled=True, use_container_width=True)
            else:
                if st.button(item["teks"], key=f"pilih_{item['id']}", use_container_width=True):
                    item["dipakai"] = True
                    st.session_state.jawaban_user.append(item)
                    st.rerun()

render_kuis_lengkap()

st.markdown("<br><hr>", unsafe_allow_html=True)

# --- TOMBOL NAVIGASI UTAMA ---
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("RESET 🔄", use_container_width=True):
        st.session_state.jawaban_user = []
        for kata in st.session_state.bank_kata:
            kata["dipakai"] = False
        st.session_state.idx_kata_dipilih = None
        st.session_state.status_periksa = False
        st.rerun()
with col2:
    if st.button("PERIKSA ✅", type="primary", use_container_width=True):
        st.session_state.status_periksa = True
with col3:
    if st.button("LANJUT ➡️", use_container_width=True):
        st.session_state.index_soal = (st.session_state.index_soal + 1) % len(st.session_state.database_soal)
        st.session_state.jawaban_user = []
        st.session_state.bank_kata = []
        st.session_state.idx_kata_dipilih = None
        st.session_state.status_periksa = False
        st.rerun()

# --- VALIDASI JAWABAN MURNI ---
if st.session_state.status_periksa:
    user_strings = [x["teks"] for x in st.session_state.jawaban_user]
    user_joined = "".join(user_strings).replace(" ", "").replace("、", "").replace("。", "").replace("【", "").replace("】", "").replace("「", "").replace("」", "").replace("Ａ", "").replace("Ｂ", "")
    kunci_joined = "".join(soal_sekarang["kunci"]).replace(" ", "").replace("、", "").replace("。", "").replace("【", "").replace("】", "").replace("「", "").replace("」", "").replace("Ａ", "").replace("Ｂ", "")

    if user_joined == kunci_joined:
        st.success(f"🎉 **正解 (Benar)!** Susunan bunpou kamu sudah sempurna!\n\n"
                   f"**🇯🇵 Kanji:** {soal_sekarang['kanji']}\n\n"
                   f"**💡 Hiragana:** {soal_sekarang['hiragana']}\n\n"
                   f"**🇮🇩 Arti:** {soal_sekarang['arti']}")
    else:
        st.error(f"❌ **残念 (Kurang Tepat).**\n\n"
                 f"**Susunan yang benar:**\n\n`{' '.join(soal_sekarang['kunci'])}`\n\n"
                 f"**🇯🇵 Kanji asli:** {soal_sekarang['kanji']}\n\n"
                 f"**💡 Hiragana:** {soal_sekarang['hiragana']}\n\n"
                 f"**🇮🇩 Arti:** {soal_sekarang['arti']}")

st.markdown("<br>", unsafe_allow_html=True)

# --- 🎯 FITUR NAVIGASI LOMPAT SOAL BULAT (1 SAMPAI 21) ---
st.write("🎯 **Lompat Instan ke Nomor Soal:**")
total_soal = len(st.session_state.database_soal)
kolom_per_baris = 7  # 7 kolom agar pas 21 soal terbagi rata menjadi 3 baris bersih

for baris_idx in range(0, total_soal, kolom_per_baris):
    baris_soal = range(baris_idx, min(baris_idx + kolom_per_baris, total_soal))
    cols_nav = st.columns(kolom_per_baris)
    
    for i, idx_s in enumerate(baris_soal):
        with cols_nav[i]:
            is_aktif = (st.session_state.index_soal == idx_s)
            tipe_tombol = "primary" if is_aktif else "secondary"
            
            if st.button(f"{idx_s + 1}", key=f"lompat_{idx_s}", type=tipe_tombol, use_container_width=True):
                st.session_state.index_soal = idx_s
                st.session_state.jawaban_user = []
                st.session_state.bank_kata = []
                st.session_state.idx_kata_dipilih = None
                st.session_state.status_periksa = False
                st.rerun()
