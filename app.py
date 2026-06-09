import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 8", layout="centered")

# --- DATABASE SOAL 100% PRESISI SESUAI FORMAT TERBARU ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # --- 1️⃣ 〜はずがない ・ 〜わけがない ---
     
        {
            "id": 1, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin... / Mustahil...)",
            "kanji": "ちゃんと約束したんだから、彼が来ないはずがない。どうしたのかなあ。",
            "hiragana": "ちゃんと やくそく した ん だ から 、 かれ が こない はず が ない 。 どうした の か なあ 。",
            "arti": "Karena sudah berjanji dengan benar, tidak mungkin dia tidak datang. Ada apa ya?",
            "kunci": ["ちゃんと", "約束", "した", "んだ", "から", "彼", "が", "来ない", "はず", "が", "ない", "。", "どう", "した", "のかなあ", "。"],
            "soal": ["ない", "の", "彼", "から", "んだ", "どう", "はず", "ちゃんと", "約束", "来ない", "が", "した", "が", "。", "した", "かなあ", "。"]
        },
        {
            "id": 2, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin... / Mustahil...)",
            "kanji": "あの店が今日休みのはずはありません。電話で確認したんですから。",
            "hiragana": "あの みせ が きょう やすみ の はず は ありません 。 でんわ で かくにん した ん です から 。",
            "arti": "Tidak mungkin toko itu hari ini libur. Karena saya sudah memastikannya lewat telepon.",
            "kunci": ["あの", "店", "が", "今日", "休み", "の", "はず", "は", "ありません", "。", "電話", "で", "確認", "した", "ん", "です", "から", "。"],
            "soal": ["休み", "Status", "確認", "で", "の", "店", "ありません", "はず", "。", "あの", "電話", "今日", "が", "した", "ん", "は", "。"]
        },
        {
            "id": 3, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin... / Mustahil...)",
            "kanji": "国家試験なのだから難しいはずがない。がんばらなくては……。",
            "hiragana": "こっかしけん な の だ から むずかしい はず が ない 。 がんばらなくては ……",
            "arti": "Karena ini adalah ujian nasional, tidak mungkin tidak sulit (pasti sulit). Saya harus berjuang...",
            "kunci": ["国家", "試験", "な", "の", "だから", "難しい", "はず", "が", "ない", "。", "がんばらなくては", "……", "。"],
            "soal": ["難しい", "試験", "国家", "な", "はず", "が", "だから", "ない", "の", "。", "がんばらなくては", "……", "。"]
        },
        {
            "id": 4, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin... / Mustahil...)",
            "kanji": "こんなに大きい家、わたしに買えるわけがないでしょう。",
            "hiragana": "こんなに おおきい いえ 、 わたし に かえる わけ が ない でしょう 。",
            "arti": "Rumah yang sebegini besar, tidak mungkin bisa kubeli, kan?",
            "kunci": ["こんなに", "大きい", "家", "わたし", "に", "買える", "わけ", "が", "ない", "でしょう", "。"],
            "soal": ["家", "大きい", "ない", "わけ", "でしょう", "わたし", "に", "買える", "こんなに", "が", "。"]
        },
        {
            "id": 5, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin... / Mustahil...)",
            "kanji": "試合に勝つために練習しているのだ。練習がきびしくないわけがない。",
            "hiragana": "しあい に かつ ため に れんしゅう して いる の だ 。 れんしゅう が きびしくない わけ が ない 。",
            "arti": "Kami berlatih demi memenangkan pertandingan. Tidak mungkin latihannya tidak keras.",
            "kunci": ["試合", "に", "勝つ", "ため", "に", "練習", "して", "いる", "の", "だ", "。", "練習", "が", "きびしくない", "わけ", "が", "ない", "。"],
            "soal": ["きびしくない", "試合", "勝つ", "の", "だ", "わけ", "ため", "して", "に", "が", "練習", "練習", "が", "いる", "に", "ない", "。", "。"]
        },
        # --- 2️⃣ 〜とは限らない ---
        {
            "id": 6, 
            "pola": "Pola 2: 〜とは限らない (Belum tentu... / Tidak selalu...)",
            "kanji": "この歌は古くから歌われているが、日本人がみんな知っているとは限らない。",
            "hiragana": "この うた は ふるく から うたわれている が 、 にほんじん が みんな しっている と は かぎらない 。",
            "arti": "Lagu ini memang sudah dinyanyikan sejak lama, tetapi belum tentu semua orang Jepang tahu.",
            "kunci": ["この", "歌", "は", "古く", "から", "歌われて", "いる", "が", "日本人", "が", "みんな", "知って", "いる", "と", "は", "限らない", "。"],
            "soal": ["歌", "古く", "知って", "が", "日本人", "この", "限らない", "は", "が", "から", "は", "みんな", "いる", "と", "歌われて", "いる", "。"]
        },
        {
            "id": 7, 
            "pola": "Pola 2: 〜とは限らない (Belum tentu... / Tidak selalu...)",
            "kanji": "値段が高いものが必ずしもいいとは限らない。",
            "hiragana": "ねだん が たかい もの が かかならずしも いい と は かぎらない 。",
            "arti": "Barang yang harganya mahal itu tidak selalu/belum tentu bagus.",
            "kunci": ["値段", "が", "高い", "物", "が", "必ずしも", "いい", "と", "は", "限らない", "。"],
            "soal": ["限らない", "物", "必ずしも", "いい", "高い", "と", "が", "値段", "が", "は", "。"]
        },
        {
            "id": 8, 
            "pola": "Pola 2: 〜とは限らない (Belum tentu... / Tidak selalu...)",
            "kanji": "旅行中にけがをしないとは限りません。保険に入っておいたほうがいいですよ。",
            "hiragana": "りょこうちゅう に けが を しない と は かぎりません 。 ほけん に はいって おいた ほう が いい です よ 。",
            "arti": "Belum tentu Anda tidak akan terluka selama perjalanan. Sebaiknya masuk asuransi saja.",
            "kunci": ["旅行", "中", "に", "けが", "を", "しない", "と", "は", "限りません", "。", "保険", "に", "入って", "おいた", "ほう", "が", "いい", "です", "よ", "。"],
            "soal": ["に", "よ", "です", "旅行", "おいた", "ほう", "しない", "限りません", "けが", "入って", "と", "保険", "中", "いい", "が", "を", "は", "に", "。", "。"]
        },
        {
            "id": 9, 
            "pola": "Pola 2: 〜とは限らない (Belum tentu... / Tidak selalu...)",
            "kanji": "新聞に書いてあることがいつも本当のこと（だ）とは限らない。",
            "hiragana": "しんぶん に かいて ある こと が いつom ほんとう の こと （だ） と は かぎらない 。",
            "arti": "Apa yang tertulis di koran tidak selalu/belum tentu benar.",
            "kunci": ["新聞", "に", "書いて", "ある", "こと", "が", "いつも", "本当", "の", "こと", "（だ）", "と", "は", "限らない", "。"],
            "soal": ["新聞", "が", "いつも", "限らない", "本当", "と", "ある", "の", "こと", "に", "は", "書いて", "こと", "（だ）", "。"]
        },
        # --- 3️⃣ 〜わけではない ・ 〜というわけではない ・ 〜のではない ---
        {
            "id": 10, 
            "pola": "Pola 3: 〜わけではない (Bukan berarti... / Bukanlah...)",
            "kanji": "長い間本をお借りしたままでしたが、忘れていたわけではありません。",
            "hiragana": "ながい あいだ ほん を おかり した まま でした が 、 わすれていた わけ で は ありません 。",
            "arti": "Saya memang meminjam buku ini dalam waktu yang lama, tetapi bukan berarti saya melupakannya.",
            "kunci": ["長い", "間", "本", "を", "お", "借り", "した", "まま", "でした", "が", "忘れて", "いた", "わけ", "で", "は", "ありません", "。"],
            "soal": ["長い", "で", "忘れて", "本", "ありません", "お", "まま", "を", "いた", "間", "でした", "わけ", "借り", "が", "は", "した", "。"]
        },
        {
            "id": 11, 
            "pola": "Pola 3: 〜わけではない (Bukan berarti... / Bukanlah...)",
            "kanji": "いつでも電話に出られるわけではありません。連絡はメールでお願いします。",
            "hiragana": "いつでも でんわ に でられる わけ で は ありません 。 れんらく は メール で おねがい します 。",
            "arti": "Bukan berarti saya bisa mengangkat telepon kapan saja. Untuk menghubungi saya, tolong lewat email saja.",
            "kunci": ["いつでも", "電話", "に", "出られる", "わけ", "で", "は", "ありません", "。", "連絡", "は", "メール", "で", "お", "願い", "します", "。"],
            "soal": ["メール", "で", "で", "電話", "いつも", "お", "わけ", "出られる", "に", "ありません", "は", "します", "は", "願い", "連絡", "。", "。"]
        },
        {
            "id": 12, 
            "pola": "Pola 3: 〜というわけではない (Bukan berarti... / Bukanlah...)",
            "kanji": "この仕事が好き（だ）というわけではないが、彼といっしょに仕事ができて楽しい。",
            "hiragana": "この しごと が すき （だ） という わけ で は ない が 、 かれ と いっしょ に しごと が できて たのしい 。",
            "arti": "Bukan berarti saya menyukai pekerjaan ini, tetapi saya senang karena bisa bekerja bersama dia.",
            "kunci": ["この", "仕事", "が", "好き", "（だ）", "という", "わけ", "で", "は", "ない", "が", "彼", "と", "いっしょ", "に", "仕事", "が", "できて", "楽しい", "。"],
            "soal": ["好き", "が", "ない", "楽しい", "わけ", "仕事", "という", "いっしょ", "この", "が", "で", "彼", "と", "できて", "（だ）", "に", "は", "が", "仕事", "。"]
        },
        {
            "id": 13, 
            "pola": "Pola 3: 〜のではない (Bukan berarti... / Bukanlah...)",
            "kanji": "転勤するのではありません。会社を辞めるんです。",
            "hiragana": "てんきん する の で は ありません 。 かいしゃ を やめる ん です 。",
            "arti": "Bukan karena pindah tugas (mutasi). Saya berhenti dari perusahaan.",
            "kunci": ["転勤", "する", "の", "で", "は", "ありません", "。", "会社", "を", "辞める", "ん", "です", "。"],
            "soal": ["会社", "転勤", "ありません", "です", "を", "辞める", "する", "で", "の", "ん", "は", "。", "。"]
        },
        {
            "id": 14, 
            "pola": "Pola 3: 〜のではない (Bukan berarti... / Bukanlah...)",
            "kanji": "Ａ「いい帽子ね。高かったでしょう。」 Ｂ「これは買ったんじゃないの。自分で作ったの。」",
            "hiragana": "Ａ「 いい ぼうし ね 。 たかかった でしょう 。」 Ｂ「 これ は かった ん じゃない の 。 じぶん で つくった の 。」",
            "arti": "A: \"Topi yang bagus ya. Pasti mahal, kan?\" B: \"Ini bukannya beli, lho. Bikin sendiri.\"",
            "kunci": ["Ａ", "「", "いい", "帽子", "ね", "。", "高かった", "でしょう", "。", "」", "Ｂ", "「", "これ", "は", "買った", "ん", "じゃ", "ない", "の", "。", "じぶん", "で", "作った", "の", "。", "」"],
            "soal": ["Ａ", "「", "高かった", "帽子", "ね", "いい", "でしょう", "。", "」", "Ｂ", "「", "ない", "の", "じぶん", "で", "買った", "これ", "は", "作った", "ん", "じゃ", "の", "。", "」"]
        },
        # --- 4️⃣ 〜ないことはない ---
        {
            "id": 15, 
            "pola": "Pola 4: 〜ないことはない (Bukan tidak... / Bisa saja asalkan...)",
            "kanji": "ここから駅まで歩けないことはありませんgが、かなり時間がかかりますよ。",
            "hiragana": "ここ から えき まで あるけない こと は ありません が 、 かなり じかん が かかります よ 。",
            "arti": "Bukan tidak bisa berjalan kaki dari sini sampai stasiun, tetapi memakan waktu yang cukup lama, lho.",
            "kunci": ["ここ", "から", "駅", "まで", "歩けない", "こと", "は", "ありません", "が", "かなり", "時間", "が", "かかります", "よ", "。"],
            "soal": ["歩けない", "から", "ありません", "時間", "駅", "かかります", "まで", "よ", "が", "は", "かなり", "ここ", "こと", "が", "。"]
        },
        {
            "id": 16, 
            "pola": "Pola 4: 〜ないことはない (Bukan tidak... / Bisa saja asalkan...)",
            "kanji": "この店のカレーもおいしくないことはないgが、わたしはもっと辛いのが好きだ。",
            "hiragana": "この みせ の カレー も おいしくない こと は ない が 、 わたし は もっと からい の が すき だ 。",
            "arti": "Kari di toko ini juga bukan tidak enak, tetapi saya lebih suka yang lebih pedas.",
            "kunci": ["この", "店", "の", "カレー", "も", "おいしくない", "こと", "は", "ない", "が", "わたし", "は", "もっと", "辛い", "の", "が", "好き", "だ", "。"],
            "soal": ["辛い", "好き", "だ", "も", "カレー", "が", "おいしくない", "の", "この", "店", "ない", "わたし", "の", "は", "もっと", "が", "こと", "は", "。"]
        },
        {
            "id": 17, 
            "pola": "Pola 4: 〜ないことはない (Bukan tidak... / Bisa saja asalkan...)",
            "kanji": "試験の結果が心配でないことはないのですが、今は終わってほっとしています。",
            "hiragana": "しけん の けっか が しんぱい で ない こと は ない の です が 、 いま は おわって ほっと して います 。",
            "arti": "Bukan berarti saya tidak khawatir dengan hasil ujiannya, tetapi sekarang saya merasa lega karena sudah selesai.",
            "kunci": ["試験", "の", "結果", "が", "心配", "で", "ない", "こと", "は", "ない", "のですが", "今", "は", "終わって", "ほっと", "して", "います", "。"],
            "soal": ["心配", "で", "います", "ない", "試験", "の", "ほっと", "です", "の", "が", "が", "今", "終わって", "して", "は", "のですが", "こと", "結果", "は", "。"]
        },
        # --- 5️⃣ 〜ことは〜が、… ---
        {
            "id": 18, 
            "pola": "Pola 5: 〜ことは〜が、… (Memang... sih, tapi...)",
            "kanji": "彼からの手紙は読んだことは読んだんですが、意味がよくわかりませんでした。",
            "hiragana": "かれ から の てがみ は よんだ こと は よんだ ん です が 、 いみ が よく わかりませんでした 。",
            "arti": "Surat dari dia memang sudah saya baca sih, tapi saya tidak begitu mengerti artinya.",
            "kunci": ["彼", "から", "の", "手紙", "は", "読んだ", "こと", "は", "読んだ", "ん", "です", "が", "意味", "が", "よく", "わかりませんでした", "。"],
            "soal": ["意味", "は", "手紙", "読んだ", "わかりませんでした", "の", "が", "よく", "読んだ", "です", "彼", "ん", "が", "は", "こと", "から", "。"]
        },
        {
            "id": 19, 
            "pola": "Pola 5: 〜ことは〜が、… (Memang... sih, tapi...)",
            "kanji": "わたしは泳げることは泳げますが、長い距離はだめなんです。",
            "hiragana": "わたし は およげる こと は およげます が 、 ながい きょり は だめ な ん です 。",
            "arti": "Saya memang bisa berenang sih, tapi kalau jarak jauh tidak bisa.",
            "kunci": ["わたし", "は", "泳げる", "こと", "は", "泳げます", "が", "長い", "距離", "は", "だめ", "な", "ん", "です", "。"],
            "soal": ["距離", "は", "泳げる", "泳げます", "わたし", "な", "は", "長い", "だめ", "です", "こと", "ん", "が", "は", "。"]
        },
        {
            "id": 20, 
            "pola": "Pola 5: 〜ことは〜が、… (Memang... sih, tapi...)",
            "kanji": "この本は高いことは高いが、写真が多くて楽しめそうだ。",
            "hiragana": "この ほん は たかい こと は たかい が 、 しゃしん が おおくて たのしめ そう だ 。",
            "arti": "Buku ini memang mahal sih, tapi sepertinya menyenangkan karena banyak fotonya.",
            "kunci": ["この", "本", "は", "高い", "こと", "は", "高い", "が", "写真", "が", "多くて", "楽しめ", "そう", "だ", "。"],
            "soal": ["写真", "だ", "多くて", "本", "高い", "は", "そう", "高い", "が", "が", "楽しめ", "この", "こと", "は", "。"]
        },
        {
            "id": 21, 
            "pola": "Pola 5: 〜ことは〜が、… (Memang... sih, tapi...)",
            "kanji": "子どもを育てるのは大変なことは大変だが、成長が楽しみで大変さを忘れる。",
            "hiragana": "こども を そだてる の は たいへん な こと は たいへん だ が 、 せいちょう が たのしみ で たいへん さ を わすれる 。",
            "arti": "Membesarkan anak memang merepotkan/berat sih, tetapi karena menantikan pertumbuhannya, rasa lelah itu pun terlupakan.",
            "kunci": ["子ども", "を", "育てる", "の", "は", "大変", "な", "こと", "は", "大変", "だ", "が", "成長", "が", "楽しみ", "で", "大変", "さ", "を", "忘れる", "。"],
            "soal": ["育てる", "を", "大変", "な", "忘れる", "成長", "の", "楽しみ", "大変", "だ", "さ", "が", "で", "は", "子ども", "が", "大変", "こと", "は", "。"]
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
    div[data-testid="stStatusWidget"] + div div[data-testid="stWidgetLabel"] { display: none; }
    [data-testid="stHorizontalBlock"] { display: flex !important; flex-direction: row !important; flex-wrap: wrap !important; gap: 6px !important; }
    [data-testid="stHorizontalBlock"] > div { flex: 1 1 22% !important; min-width: 70px !important; }
    .info-box { background-color: #e8f4fd; padding: 15px; border-radius: 12px; border-left: 5px solid #1fa2ff; margin-bottom: 20px; }
    .text-bunpou { font-size: 1.05rem; font-weight: bold; color: #1fa2ff; margin: 0 0 6px 0; }
    .text-arti { font-size: 1.2rem; font-weight: bold; color: #1a1a1a; margin: 0; }
    div.stButton > button { border-radius: 12px !important; font-weight: bold !important; padding: 6px 10px !important; }
    .swap-indicator { background-color: #e6fffa; border: 1px dashed #319795; padding: 10px; border-radius: 8px; color: #234e52; font-weight: bold; margin-bottom: 10px; font-size: 0.9rem; }
    .stButton > button[key^="lompat_"] { border-radius: 50% !important; width: 40px !important; height: 40px !important; padding: 0 !important; display: flex !important; align-items: center !important; justify-content: center !important; }
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

@st.fragment
def render_kuis_lengkap():
    st.write("### Kalimat Susunanmu:")
    mode = st.radio("Aksi Sentuhan Papan:", ["Copot Kata (Normal)", "Tukar Posisi 2 Kata 🔄"], horizontal=True, label_visibility="collapsed")
    
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
        klik_papan = st.pills(label="Papan Jawaban", options=opsi_papan, format_func=lambda x: format_papan[x], selection_mode="single", label_visibility="collapsed")
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

# --- VALIDASI KARAKTER AMAN ---
if st.session_state.status_periksa:
    user_strings = [x["teks"] for x in st.session_state.jawaban_user]
    user_joined = "".join(user_strings).replace(" ", "").replace("、", "").replace("。", "").replace("「", "").replace("」", "").replace("（", "").replace("）", "").replace("だ", "").replace("Ａ", "").replace("Ｂ", "").replace("…", "")
    kunci_joined = "".join(soal_sekarang["kunci"]).replace(" ", "").replace("、", "").replace("。", "").replace("「", "").replace("」", "").replace("（", "").replace("）", "").replace("だ", "").replace("Ａ", "").replace("Ｂ", "").replace("…", "")

    if user_joined == kunci_joined:
        st.success(f"🎉 **正解 (Benar)!**\n\n**🇯🇵 Kanji:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}\n\n**🇮🇩 Arti:** {soal_sekarang['arti']}")
    else:
        st.error(f"❌ **残念 (Kurang Tepat).**\n\n**Susunan yang benar:**\n\n`{' '.join(soal_sekarang['kunci'])}`\n\n**🇯🇵 Kanji asli:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}\n\n**🇮🇩 Arti:** {soal_sekarang['arti']}")

st.markdown("<br>", unsafe_allow_html=True)
st.write("🎯 **Lompat Instan ke Nomor Soal:**")
total_soal = len(st.session_state.database_soal)
kolom_per_baris = 7

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
