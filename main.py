import streamlit as st
from PIL import Image

# ページ設定を初期化
st.set_page_config(page_title="Cafe Ritsuan", layout="wide")

# 言語データの辞書
languages = {
    "English": {
        "title": "Cafe Ritsuan",
        "caption": "Coffee and Light Meals",
        "tab_meals": "Meals",
        "tab_drinks": "Drinks",
        "tab_others": "Others",
        "tab_info": "Store Information",
        "info_content": "Welcome to Cafe Ritsuan! Here we focus on high-quality coffee and fresh light meals. Our cozy environment is perfect for catching up with friends or for a quick meeting. Don't miss our homemade cakes!"
    },
    "Japanese": {
        "title": "カフェリツアン",
        "caption": "コーヒーと軽食",
        "tab_meals": "食事",
        "tab_drinks": "ドリンク",
        "tab_others": "その他",
        "tab_info": "お店情報",
        "info_content": "カフェリツアンへようこそ！当店は高品質なコーヒーと新鮮な軽食を提供しています。居心地の良い環境は、友人との再会やちょっとした会議に最適です。自家製ケーキをお見逃しなく！"
    }
}

# メニュー項目も多言語に対応
menu_items = {
    "食事": [
        {
            "name": {"English": "Toast Set", "Japanese": "トーストセット"},
            "price": "500円",
            "description": {
                "English": "Freshly baked toast served with a fried egg and salad.",
                "Japanese": "焼きたてのトーストに、目玉焼きとサラダが付きます。"
            },
            "image_path": "public/toast_set.jpg"
        },
        {
            "name": {"English": "Vegetable Sandwich", "Japanese": "ベジタブルサンド"},
            "price": "600円",
            "description": {
                "English": "A healthy sandwich packed with fresh vegetables.",
                "Japanese": "新鮮な野菜をふんだんに使用したヘルシーなサンドイッチ。"
            },
            "image_path": "public/vegetable_sandwich.jpg"
        }
    ],
    "ドリンク": [
        {
            "name": {"English": "Cafe Latte", "Japanese": "カフェラテ"},
            "price": "400円",
            "description": {
                "English": "A classic combination of espresso and steamed milk.",
                "Japanese": "エスプレッソとスチームミルクのクラシックなコンビネーション。"
            },
            "image_path": "public/cafe_latte.jpg"
        },
        {
            "name": {"English": "Matcha Latte", "Japanese": "抹茶ラテ"},
            "price": "450円",
            "description": {
                "English": "A fine matcha latte with a perfect balance of sweetness and bitterness.",
                "Japanese": "上質な抹茶を使用した、甘みと苦みが絶妙な和風ラテ。"
            },
            "image_path": "public/matcha_latte.jpg"
        }
    ],
    "その他": [
        {
            "name": {"English": "Chocolate Cake", "Japanese": "チョコレートケーキ"},
            "price": "400円",
            "description": {
                "English": "A rich and creamy homemade chocolate cake.",
                "Japanese": "リッチでクリーミーな自家製チョコレートケーキ。"
            },
            "image_path": "public/chocolate_cake.jpg"
        },
        {
            "name": {"English": "Fruit Parfait", "Japanese": "フルーツパフェ"},
            "price": "500円",
            "description": {
                "English": "A colorful and delicious parfait made with seasonal fruits.",
                "Japanese": "季節のフルーツを使ったカラフルで美味しいパフェ。"
            },
            "image_path": "public/fruit_parfait.jpg"
        }
    ]
}

# いいね！数とコメントを記録するディクショナリ
like_counts = {}
comments = {}


def display_menu_item(item, language):
    with st.expander(f"{item['name'][language]} - {item['price']}"):
        st.write(item['description'][language])
        image = Image.open(item['image_path'])
        st.image(image, caption=item['name'][language], use_column_width=True)

        # いいね！ボタン
        like_key = f"like_{item['name'][language]}"
        if st.button('👍', key=like_key):
            like_counts[like_key] = like_counts.get(like_key, 0) + 1
        st.write(f"{like_counts.get(like_key, 0)} likes")

        # コメント機能
        comment_key = f"comment_{item['name'][language]}"
        new_comment = st.text_input("Leave a comment", key=f"input_{comment_key}")
        if st.button("Post", key=f"btn_{comment_key}"):
            if comment_key in comments:
                comments[comment_key].append(new_comment)
            else:
                comments[comment_key] = [new_comment]
        for comment in comments.get(comment_key, []):
            st.write(comment)


def main():
    # 言語選択
    selected_language = st.sidebar.selectbox("Choose Language", options=["English", "Japanese"])

    # 言語に基づいたテキストの表示
    st.title(languages[selected_language]["title"])
    st.caption(languages[selected_language]["caption"])

    # タブの設定
    tab1, tab2, tab3, tab4 = st.tabs([
        languages[selected_language]["tab_info"],
        languages[selected_language]["tab_meals"],
        languages[selected_language]["tab_drinks"],
        languages[selected_language]["tab_others"]
    ])

    # 各タブの中身の表示
    with tab1:
        st.header(languages[selected_language]["tab_info"])
        st.write(languages[selected_language]["info_content"])

    with tab2:
        st.header(languages[selected_language]["tab_meals"])
        for item in menu_items["食事"]:
            display_menu_item(item, selected_language)

    with tab3:
        st.header(languages[selected_language]["tab_drinks"])
        for item in menu_items["ドリンク"]:
            display_menu_item(item, selected_language)

    with tab4:
        st.header(languages[selected_language]["tab_others"])
        for item in menu_items["その他"]:
            display_menu_item(item, selected_language)

if __name__ == "__main__":
    main()
