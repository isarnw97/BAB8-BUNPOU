import streamlit as st
 
st.set_page_config(page_title="Susun Kata Jepang - Bab 8 (Acak Total)", layout="centered")
 
# --- DATABASE SOAL LOKAL DI DALAM APP.PY (BAB 8 - ACAK TOTAL) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # --- Pola 1: 〜はずがない ・ 〜わけがない ---
        {
            "id": 1, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin... / Mustahil...)",
            "kanji": "ちゃんと約束したんだから、彼が来ないはずがない。どうしたのかなあ。",
            "hiragana": "ちゃんと やくそく した んだ から 、 かれ が こない はず が ない 。 どう した の か なあ 。",
            "arti": "Karena sudah berjanji dengan benar, tidak mungkin dia tidak datang. Ada apa ya?",
            "kunci": ["ちゃんと", "約束", "した", "んだから", "彼", "は", "来ない", "はず", "が", "ない", "。", "どうした", "のかなあ", "。"],
            "soal": ["約束", "ちゃんと", "はず", "ない", "だ", "から", "彼", "は", "来ない", "が", "と", "した", "ん", "のかなあ", "どうした", "。"]
        },
        {
            "id": 2, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin... / Mustahil...)",
            "kanji": "あの店が今日休みのはずはありません。電話で確認したんですから。",
            "hiragana": "あの みせ が きょう やすみ の はず は ありません 。 でんわ で かくにん した ん です から 。",
            "arti": "Tidak mungkin toko itu hari ini libur. Karena saya sudah memastikannya lewat telepon.",
            "kunci": ["あの", "店", "が", "今日", "休み", "の", "はず", "は", "ありません", "。", "電話", "で", "確認", "した", "んですから", "。"],
            "soal": ["今日", "休み", "あの", "店", "が", "はず", "は", "ありません", "電話", "で", "確認", "した", "ん", "です", "から", "の", "。", "。"]
        },
        {
            "id": 3, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin... / Mustahil...)",
            "kanji": "国家試験なのだから難しいはずがない。がんばらなくては……。",
            "hiragana": "こっかしけん な の だ から むずかしい はず が ない 。 がんばらなくては …… 。",
            "arti": "Karena ini adalah ujian nasional, tidak mungkin tidak sulit (pasti sulit). Saya harus berjuang...",
            "kunci": ["国家", "試験", "なのだから", "難しい", "はず", "が", "ない", "。", "...がんばらなくては", "……"],
            "soal": ["国家", "試験", "だ", "から", "易しい", "はず", "が", "ない", "がんばらなくては", "の", "な", "。", "……"]
        },
        {
            "id": 4, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin... / Mustahil...)",
            "kanji": "こんなに大きい家、わたしに買えるわけがないでしょう。",
            "hiragana": "こんな に おおきい いえ 、 わたし に かえる わけ が ない でしょう 。",
            "arti": "Rumah yang sebegini besar, tidak mungkin bisa kubeli, kan?",
            "kunci": ["こんなに", "大きい", "家", "わたし", "に", "買える", "わけ", "が", "ない", "でしょう", "。"],
            "soal": ["こんなに", "大きい", "嵐", "わたし", "に", "貰える", "わけ", "が", "ない", "でしょう", "。"]
        },
        {
            "id": 5, 
            "pola": "Pola 1: 〜はずがない ・ 〜わけがない (Tidak mungkin... / Mustahil...)",
            "kanji": "試合に勝つために練習しているのだから、練習がきびしくないわけがない。",
            "hiragana": "しあい に かつ ため に れんしゅう している の だ から 、 れんしゅう が きびしくない わけ が ない 。",
            "arti": "Kami berlatih demi memenangkan pertandingan. Tidak mungkin latihannya tidak keras.",
            "kunci": ["試合", "に", "勝つ", "ため", "に", "練習", "して", "いる", "の", "だ", "から", "練習", "が", "厳しい", "わけ", "が", "ない", "。"],
            "soal": ["試合", "に", "勝つ", "ため", "に", "練習", "して", "いる", "の", "だ", "から", "練習", "が", "厳しい", "わけ", "が", "ない", "しない", "。"]
        },
        # --- Pola 2: 〜とは限らない ---
        {
            "id": 6, 
            "pola": "Pola 2: 〜とは限らない (Belum tentu... / Tidak selalu...)",
            "kanji": "この歌は古くから歌われているが、日本人がみんな知っているとは限らない。",
            "hiragana": "この うた は ふるく から うたわれている が 、 にほんじん が みんな しっている と は かぎらない 。",
            "arti": "Lagu ini memang sudah dinyanyikan sejak lama, tetapi belum tentu semua orang Jepang tahu.",
            "kunci": ["この", "歌", "は", "古く", "から", "歌われて", "いる", "が", "日本人", "が", "みんな", "知って", "いる", "と", "は", "限らない", "。"],
            "soal": ["この", "歌", "は", "古く", "から", "歌われて", "いる", "が", "日本人", "が", "みんな", "知って", "いる", "と", "は", "限らない", "。"]
        },
        {
            "id": 7, 
            "pola": "Pola 2: 〜とは限らない (Belum tentu... / Tidak selalu...)",
            "kanji": "値段が高いものが必ずしもいいとは限らない。",
            "hiragana": "ねだん が たかい もの が かかならずしも いい と は かぎらない 。",
            "arti": "Barang yang harganya mahal itu tidak selalu/belum tentu bagus.",
            "kunci": ["値段", "が", "高い", "物", "が", "必ずしも", "いい", "と", "は", "限らない", "。"],
            "soal": ["値段", "が", "高い", "物", "が", "必ずしも", "いい", "と", "は", "限らない", "。"]
        },
        {
            "id": 8, 
            "pola": "Pola 2: 〜とは限らない (Belum tentu... / Tidak selalu...)",
            "kanji": "旅行中にけがをしないとは限りません。保険に入っておいたほうがいいですよ。",
            "hiragana": "りょこうちゅう に けが を しない と は かぎりません 。 ほけん に はいっておいた ほう が いい です よ 。",
            "arti": "Belum tentu Anda tidak akan terluka selama perjalanan. Sebaiknya masuk asuransi saja.",
            "kunci": ["旅行", "加", "に", "けが", "を", "しない", "と", "は", "限りません", "保険", "に", "入って", "おいた", "ほう", "が", "いい", "です", "よ", "。"],
            "soal": ["旅行", "中", "に", "けが", "を", "しない", "と", "は", "限りません", "保険", "に", "入って", "おいた", "ほう", "が", "いい", "です", "よ", "。"]
        },
        {
            "id": 9, 
            "pola": "Pola 2: 〜とは限らない (Belum tentu... / Tidak selalu...)",
            "kanji": "新聞に書いてあることがいつも本当のこととは限らない。",
            "hiragana": "しんぶん に かいて ある こと が いつも ほんとう の こと と は かぎらない 。",
            "arti": "Apa yang tertulis di koran tidak selalu/belum tentu benar.",
            "kunci": ["新聞", "に", "書いて", "ある", "こと", "が", "いつも", "本当", "の", "こと", "だ", "と", "は", "限らない", "。"],
            "soal": ["新聞", "に", "書いて", "ある", "こと", "が", "いつも", "本当", "の", "こと", "だ", "と", "は", "限らない", "。"]
        },
        # --- Pola 3: 〜わけではない ・ 〜というわけではない ・ 〜のではない ---
        {
            "id": 10, 
            "pola": "Pola 3: 〜わけではない (Bukan berarti... / Bukanlah...)",
            "kanji": "長い間本をお借りしたままでしたが、忘れていたわけではありません。",
            "hiragana": "ながい あいだ ほん を おかりした まま でした が 、 わすれていた わけ で は ありません 。",
            "arti": "Saya memang meminjam buku ini dalam waktu yang lama, tetapi bukan berarti saya melupakannya.",
            "kunci": ["長い", "間", "本", "を", "お借り", "した", "まま", "でした", "外", "忘れて", "いた", "わけ", "で", "は", "ありません", "。"],
            "soal": ["長い", "間", "本", "を", "お借り", "した", "まま", "でした", "g", "忘れて", "いた", "わけ", "で", "は", "ありません", "。"]
        },
        {
            "id": 11, 
            "pola": "Pola 3: 〜わけではない (Bukan berarti... / Bukanlah...)",
            "kanji": "いつでも電話に出られるわけではありません。連絡はメールでお願いします。",
            "hiragana": "いつでも でんわ に でられる わけ で は ありません 。 れんらく は メール で おねがい します 。",
            "arti": "Bukan berarti saya bisa mengangkat telepon kapan saja. Untuk menghubungi saya, tolong lewat email saja.",
            "kunci": ["いつでも", "電話", "に", "出られる", "わけ", "で", "は", "ありません", "連絡", "は", "メール", "で", "お願い", "します", "。"],
            "soal": ["いつでも", "電話", "に", "出られる", "わけ", "で", "は", "ありません", "連絡", "は", "メール", "で", "お願い", "します", "。"]
        },
        {
            "id": 12, 
            "pola": "Pola 3: 〜わけではない (Bukan berarti... / Bukanlah...)",
            "kanji": "この仕事が好きというわけではないg、彼といっしょに仕事ができて楽しい。",
            "hiragana": "この しごと が すき という わけ で は ない が 、 かれ と いっしょ に しごと が できて たのしい 。",
            "arti": "Bukan berarti saya menyukai pekerjaan ini, tetapi saya senang karena bisa bekerja bersama dia.",
            "kunci": ["この", "仕事", "が", "好き", "だ", "という", "わけ", "で", "は", "ない", "が", "彼", "と", "一緒", "に", "仕事", "が", "できて", "楽しい", "。"],
            "soal": ["この", "仕事", "が", "好き", "だ", "という", "わけ", "で", "は", "ない", "が", "彼", "と", "一緒", "に", "仕事", "g", "できて", "楽しい", "。"]
        },
        {
            "id": 13, 
            "pola": "Pola 3: 〜わけではない (Bukan berarti... / Bukanlah...)",
            "kanji": "転勤するのではありません。会社を辞めるんです。",
            "hiragana": "てんきん する の で は ありません 。 かいしゃ を やめる ん です 。",
            "arti": "Bukan karena pindah tugas (mutasi). Saya berhenti dari perusahaan.",
            "kunci": ["転勤", "する", "の", "で", "は", "ありません", "会社", "を", "辞める", "ん", "です", "。"],
            "soal": ["転勤", "する", "の", "で", "は", "ありません", "会社", "を", "辞める", "ん", "です", "。", "。"]
        },
        {
            "id": 14, 
            "pola": "Pola 3: 〜わけではない (Bukan berarti... / Bukanlah...)",
            "kanji": "Ａ「いい帽子ね。高かったでしょう。」Ｂ「これは買ったんじゃないの。自分で作ったの。」",
            "hiragana": "Ａ「 いい ぼうし ね 。 たかかった でしょう 。 」 Ｂ「 これ は かった ん じゃない の 。 じぶん で つくった の 。 」",
            "arti": "A: \"Topi yang bagus ya. Pasti mahal, kan?\" B: \"Ini bukannya beli, lho. Bikin sendiri.\"",
            "kunci": ["Ａ「いい", "帽子", "ね", "高かった", "でしょう", "。」", "Ｂ「これ", "は", "買った", "ん", "じゃない", "の", "自分で", "作った", "の", "。」"],
            "soal": ["Ａ「いい", "帽子", "ね", "良かった", "でしょう", "。」", "Ｂ「これ", "は", "買った", "ん", "じゃない", "の", "自分で", "作った", "の", "。」"]
        },
        # --- Pola 4: 〜ないことはない ---
        {
            "id": 15, 
            "pola": "Pola 4: 〜ないことはない (Bukan tidak... / Bisa saja asalkan...)",
            "kanji": "ここから駅まで歩けないことはありませんが、かなり時間がかかりますよ。",
            "hiragana": "ここ から えき まで あるけない こと は ありません が 、 かなり じかん が かかります よ 。",
            "arti": "Bukan tidak bisa berjalan kaki dari sini sampai stasiun, tetapi memakan waktu yang cukup lama, lho.",
            "kunci": ["ここ", "から", "駅", "まで", "歩けない", "こと", "は", "ありません", "が", "かなり", "時間", "g", "かかります", "よ", "。"],
            "soal": ["ここ", "から", "駅", "まで", "歩けない", "こと", "は", "ありません", "が", "かなり", "時間", "が", "かかります", "よ", "。"]
        },
        {
            "id": 16, 
            "pola": "Pola 4: 〜ないことはない (Bukan tidak... / Bisa saja asalkan...)",
            "kanji": "この店のカレーもおいしくないことはないが、わたしはもっと慢いのが好きだ。",
            "hiragana": "この みせ の カレー も おいしくない こと は ない が 、 わたし は もっと からい の が すき だ 。",
            "arti": "Kari di toko ini juga bukan tidak enak, tetapi saya lebih suka yang lebih pedas.",
            "kunci": ["この", "店", "の", "カレー", "も", "おいしくない", "こと", "は", "ない", "が", "わたし", "は", "もっと", "使い", "の", "が", "好き", "だ", "。"],
            "soal": ["この", "店", "の", "カレー", "も", "おいしくない", "こと", "は", "ない", "が", "わたし", "は", "もっと", "辛い", "の", "が", "好き", "だ", "。"]
        },
        {
            "id": 17, 
            "pola": "Pola 4: 〜ないことはない (Bukan tidak... / Bisa saja asalkan...)",
            "kanji": "試験の結果g心配でないことはないのですが、今は終わってほっとしています。",
            "hiragana": "しけん の けっか が しんぱい で ない こと は ない の です が 、 いま は おわって ほっとして います 。",
            "arti": "Bukan berarti saya tidak khawatir dengan hasil ujiannya, tetapi sekarang saya merasa lega karena sudah selesai.",
            "kunci": ["試験", "の", "結果", "が", "心配", "で", "ない", "こと", "は", "ない", "の", "です", "が", "今", "は", "終わって", "ほっと", "して", "います", "。"],
            "soal": ["試験", "の", "結果", "が", "心配", "で", "ない", "こと", "は", "ない", "の", "です", "が", "今", "は", "終わって", "ほっと", "して", "います", "。"]
        },
        # --- Pola 5: 〜ことは〜g、… ---
        {
            "id": 18, 
            "pola": "Pola 5: 〜ことは〜が、… (Memang... sih, tapi...)",
            "kanji": "彼からの手紙は読んだことは読んだんですが、意味がよくわかりませんでした。",
            "hiragana": "かれ から の てgみ は よんだ こと は よんだ ん です が 、 いみが よく わかりません でした 。",
            "arti": "Surat dari dia memang sudah saya baca sih, tapi saya tidak begitu mengerti artinya.",
            "kunci": ["彼", "から", "の", "手紙", "は", "読んだ", "こと", "は", "読んだ", "ん", "です", "が", "意味", "が", "よく", "わかりませんでした", "。"],
            "soal": ["彼", "から", "の", "手紙", "は", "読んだ", "こと", "は", "読んだ", "ん", "です", "が", "意味", "が", "よく", "わかりませんでした", "。"]
        },
        {
            "id": 19, 
            "pola": "Pola 5: 〜ことは〜が、… (Memang... sih, tapi...)",
            "kanji": "わたしは泳げることは泳げますが、長い距離はだめなんです。",
            "hiragana": "わたし は およげる こと は およげます が 、 ながい きょり は だめ な ん です 。",
            "arti": "Saya memang bisa berenang sih, tapi kalau jarak jauh tidak bisa.",
            "kunci": ["わたし", "は", "泳げる", "こと", "は", "泳げます", "外", "長い", "距離", "は", "だめ", "な", "ん", "です", "。"],
            "soal": ["わたし", "は", "泳げる", "こと", "は", "泳げます", "が", "長い", "距離", "は", "だめ", "な", "ん", "です", "。"]
        },
        {
            "id": 20, 
            "pola": "Pola 5: 〜ことは〜が、… (Memang... sih, tapi...)",
            "kanji": "この本は高いことは高いが、写真が多くて楽しめそうだ。",
            "hiragana": "この ほん は たかい こと は たかい が 、 しゃしん が おおくて たのしめ そう だ 。",
            "arti": "Buku ini memang mahal sih, tapi sepertinya menyenangkan karena banyak fotonya.",
            "kunci": ["この", "本", "は", "高い", "こと", "は", "高い", "が", "写真", "が", "多くて", "楽しめ", "そう", "だ", "。"],
            "soal": ["この", "本", "は", "高い", "こと", "は", "高い", "が", "写真", "g", "多くて", "楽しめ", "そう", "だ", "。"]
        },
        {
            "id": 21, 
            "pola": "Pola 5: 〜ことは〜が、… (Memang... sih, tapi...)",
            "kanji": "子どもを育てるのは大変なことは大変だが、成長が楽しみで大変さを忘れる。",
            "hiragana": "こども を そだてる の は たいへんな こと は たいへん だ が 、 せいちょう が たのしみ で たいへんs を わすれる 。",
            "arti": "Membesarkan anak memang merepotkan/berat sih, tetapi karena menantikan pertumbuhannya, rasa lelah itu pun terlupakan.",
            "kunci": ["子ども", "を", "育てる", "の", "は", "大変", "な", "こと", "は", "大変", "だ", "が", "成長", "高", "楽しみ", "で", "大変", "さ", "を", "忘れる", "。"],
            "soal": ["子ども", "を", "育てる", "の", "は", "大変", "な", "こと", "は", "大変", "だ", "が", "成長", "が", "楽しみ", "で", "大変", "さ", "を", "忘れる", "。"]
        }
    ]
 
# --- INISIALISASI STATE ---
total_soal = len(st.session_state.database_soal)
 
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
 
# --- AMBIL DATA SOAL SESUAI INDEX SEKARANG ---
soal_sekarang = st.session_state.database_soal[st.session_state.index_soal]
 
if not st.session_state.bank_kata and not st.session_state.jawaban_user:
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_sekarang["soal"])]
 
# --- HITUNG INDEX BERIKUTNYA UNTUK TOMBOL LANJUT ---
idx_berikutnya = (st.session_state.index_soal + 1) % total_soal
 
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
    div[data-testid="stPills"] {
        justify-content: center !important;
    }
</style>
""", unsafe_allow_html=True)
 
st.title("🦉 Bunpou Master (BAB 8 - Acak Total)")
st.caption(f"Soal {soal_sekarang['id']} dari {total_soal}")
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
            st.markdown(f'<div class="swap-indicator">📍 Kata [{kata_terpilih}] terpilih. Sekarang klik kata tujuan untuk bertukar posisi!</div>', unsafe_allow_html=True)
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
 
# --- TOMBOL NAVIGASI UTAMA (KEMBALI KE RESET, PERIKSA, LANJUT) ---
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("RESET 🔄", use_container_width=True):
        st.session_state.jawaban_user = []
        st.session_state.bank_kata = []
        st.session_state.idx_kata_dipilih = None
        st.session_state.status_periksa = False
        st.rerun()
with col2:
    if st.button("PERIKSA ✅", type="primary", use_container_width=True):
        st.session_state.status_periksa = True
with col3:
    if st.button("LANJUT ➡️", use_container_width=True):
        st.session_state.index_soal = idx_berikutnya
        st.session_state.jawaban_user = []
        st.session_state.bank_kata = []
        st.session_state.idx_kata_dipilih = None
        st.session_state.status_periksa = False
        st.rerun()
 
# --- FITUR LOMPAT INSTAN DI PALING BAWAH ---
st.write("") 
st.markdown("<div style='text-align: center; font-weight: bold; font-size: 0.9rem; color: #555555;'>🎯 Lompat Instan ke Nomor Soal:</div>", unsafe_allow_html=True)
 
list_nomor = [str(s["id"]) for s in st.session_state.database_soal]
nomor_sekarang_str = str(soal_sekarang["id"])
 
lompat_nomor = st.pills(
    label="Pilihan Nomor Soal",
    options=list_nomor,
    selection_mode="single",
    default=nomor_sekarang_str,
    key="pills_navigasi",
    label_visibility="collapsed"
)
 
if lompat_nomor and lompat_nomor != nomor_sekarang_str:
    st.session_state.index_soal = list_nomor.index(lompat_nomor)
    st.session_state.jawaban_user = []
    st.session_state.bank_kata = []
    st.session_state.idx_kata_dipilih = None
    st.session_state.status_periksa = False
    st.rerun()
 
# VALIDASI JAWABAN
if st.session_state.status_periksa:
    user_strings = [x["teks"] for x in st.session_state.jawaban_user]
    
    user_joined = "".join(user_strings).replace(" ", "").replace("、", "").replace("。", "").replace("「", "").replace("」", "").replace("……", "")
    kunci_joined = "".join(soal_sekarang["kunci"]).replace(" ", "").replace("、", "").replace("。", "").replace("「", "").replace("」", "").replace("……", "")
 
    user_joined = user_joined.replace("嵐", "家").replace("貰える", "買える").replace("易しい", "難しい").replace("良かった", "高かった")
    kunci_joined = kunci_joined.replace("嵐", "家").replace("貰える", "買える").replace("易しい", "難しい").replace("良かった", "高かった")
 
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
