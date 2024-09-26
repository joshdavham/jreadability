from jreadability import compute_readability

class Test_jreadability:

    def test_upper_intermediate(self):

        upper_intermediate_text = """アレルギー体質の人が、長年スギの花粉を吸っていると、免疫反応が過剰に起こり、目、鼻の粘膜を刺激し、目が充血して、涙やくしゃみが止まらなくなる。この病気は30年ほど前に発見された。アンケート分析によると日本人の10人に3人は花粉症に悩まされているそうだ。アレルギー症状は、鼻、目が圧倒的に多く、その他、のど、皮膚、気管支などにも出る。マスクの女性が出たら、アレルギー体質の人は外出をひかえるか、花粉が目、鼻、口に入らないようにサングラスやマスクをしたうえで風の向きや強さに気をつけて、外出したほうがいいだろう。
        スギの花粉が風に乗って飛び散る様子を見たことがある。強い風が吹くと、何千本というスギの雄花から花粉が一斉に吹き飛ばされる。米粒大の雄花の一つ一つに約40万個の花粉が詰まっている。この花粉が、霞のようにたなびいて、スギの林が見えなくなるほどだ。花粉症をおこす草花は、北アメリカではブタクサ、ヨーロッパではカバの木やコナラなどだが、日本では花粉症の8割をスギ花粉症が占めている。
        それは日本にスギの木が多いからだ。理由は二つある。第一の理由は、第二次世界大戦後、日本は荒れた国土を緑にしようと、スギの苗を全国各地に植えた。20年後、そのスギが育ち、毎年春になると花粉が飛ぶようになったからだ。第二の理由は、日本人の食生活が欧米風になって、アレルギーを起こしやすくなったからだと言われている。スギ花粉症は、まさに日本人の現代病と言えるだろう。花粉症は薬で、症状を軽くおさえることができる。またスギの花粉が飛ぶのは、2月初めから4月にかけてで、この季節が終われば自然になおる。それで、このシーズンが来ると、都内のデパートには花粉症対策グッズコーナーがお目見えし、メーカー各社からは、新型マスクから情報提供までの「花粉症商戦」が花盛りとなる。"""

        score = compute_readability(upper_intermediate_text)

        assert 2.5 <= score < 3.4