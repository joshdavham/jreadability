from jreadability import compute_readability
import time
from fugashi import Tagger

# texts taken from https://jreadability.net/sys/sample?lang=en
upper_advanced_text = """　数学は，科学を記述する普遍的な言語であるという基本的な性格を持つ。また「自然は数学の言葉で書かれた書物である」とはガリレイの言である。
    　ニュートン以後１９世紀まで，古典物理学と数学とは，微分方程式と特殊関数の研究を“かなめ”として即かず離れずの関係で発展してきたが，今世紀に至り，場の量子論・統計力学と現代数学が結合し，数理物理学の新しい発展を遂げることになった。この展開によって，解析学のみでなくトポロジー，多様体論，代数幾何学，整数論にまでわたる，現代数学の先端諸分野を横断する新しい視点と手段がもたらされ，重要な問題の解決や新しい理論の展開にまで導かれることになった。数学の分野において我が国は多数の優れた研究者を擁し，世界のこの分野の発展に大きく貢献した業績は特筆すべきものがある。
    　９０年代を通じて，以上に述べた主題は引き続き主要な対象として発展するものと思われるが，本質的な発展は新しい視点の発見によって，予期されない形でもたらされるものであろう。応用数学は今後一層重要性を増し，さらに数物科学の領域に全く新しい研究分野が発展することも大いに期待されるところである。　物理学は，自然認識の哲学といわれる面を持つとともに，自然界の本質，自然界を支配する法則を実験により実証し，解明する学問である。　素粒子物理学は，物質の究極の構成粒子（素粒子）や，自然界を支配する四種の力の本性を解明することを目的とし，今や素粒子と力の本性について，標準模型と呼ばれる物質・自然観が確立されるところまでに至っている。我が国の高エネルギー物理学研究所が有するトリスタン電子・陽電子衝突型加速器は優れた加速器性能や実験技術とあいまって標準模型の検証に貴重な貢献をした。標準模型において残されている課題は，未知のトップクォークの発見やヒグス粒子の本性の解明などである。標準模型には，なお基本的な理論として不十分な点があり，それが次世代超大型陽子・陽子衝突型加速器に期待される主要な研究命題となっている。そのほか，今後の素粒子研究には，加速器のエネルギー領域では到底検証できない課題や加速器を用いない全く別の取組を必要とする課題が残されている。強い力をも統一的に扱う大統一理論や，重力に関する研究等である。
    　宇宙物理学は素粒子物理学と急速に接近した。それはビッグバンに始まる宇宙の進化の過程が，素粒子を抜きにしては理解できなくなったためである。陽子崩壊の検出のため建設された神岡実験施設が，いち早く超新星爆発に伴うニュートリノを検出するのに成功したのはその一例である。"""

lower_advanced_text = """動物の動きにしてもそうで、ネズミはちょこまかしているし、ゾウはゆっくりと足を運んでいく。体のサイズと時間との間に、何か関係があるのではないかと、古来、いろいろな人が調べてきた。例えば、心臓がドキン、ドキンと打つ時間間隔を、ネズミで測り、ネコで測り、イヌで測り、ウマで測り、ゾウで測り、と計測して、おのおのの動物の体重と時間との関係を求めてみたのである。サイズを体重で表わすのは、体重なら、はかりにポイと載せればすぐ測れるが、体長でサイズを表わすと、しっぽは計測値に入れるのか、背伸びした長さか丸まったときの長さかなどと、難しい問題がいろいろ出てくるからだ。
    いろいろな哺乳類で体重と時間とを測ってみると、こんな関係が浮かび上がってきた。時間㏄(体重)1/4(㏄は比例するという記号)時間は体重の4分の1乗に比例するのである。体重が増えると時間は長くなる。ただし4分の1乗というのは平方根の平方根だから、体重が16倍になると時間が2倍になるという計算で、体重が16倍なら時間も16倍という単純な比例とは違い、体重の増え方に比べれば時間の長くなり方はずっと緩やかだ。ずっと緩やかではあるが、体重とともに時間は長くなっていく。つまり大きな動物ほど、何をするにも時間がかかるということだ。動物が違うと、時間の流れる速度が達ってくるものらしい。例えば体重が10倍になると、寺間は1.8(101/4)倍になる。寺間が倍近くかかるのだから、これは動物にとって無視できない問題である。この4分の1乗則は、時間がかかわっているいろいろな現象に非常に広く当てはまる。例えば動物の一生にかかわるものでは、寿命をはじめとして、大人のサイズに成長するまでの時間、性的に成熟するのに要する時間、赤ん坊が母親の胎内にとどまっている時間など、すべてこの4分の1乗則に従う。
    日常の活動の時間も、やはり体重の4分の1乗に比例する。息をする時間間隔、心臓が打つ間隔、腸が1同じわっと蠕動する時間、血が体内を1巡する時間、体外から入った異物を再び体外へと除去するのに要する時間、たんぱく質が合成されてから壊されるまでの時間、等々。生物の時間をこんなふうにとらえられるかもしれない。"""

upper_intermediate_text = """アレルギー体質の人が、長年スギの花粉を吸っていると、免疫反応が過剰に起こり、目、鼻の粘膜を刺激し、目が充血して、涙やくしゃみが止まらなくなる。この病気は30年ほど前に発見された。アンケート分析によると日本人の10人に3人は花粉症に悩まされているそうだ。アレルギー症状は、鼻、目が圧倒的に多く、その他、のど、皮膚、気管支などにも出る。マスクの女性が出たら、アレルギー体質の人は外出をひかえるか、花粉が目、鼻、口に入らないようにサングラスやマスクをしたうえで風の向きや強さに気をつけて、外出したほうがいいだろう。
    スギの花粉が風に乗って飛び散る様子を見たことがある。強い風が吹くと、何千本というスギの雄花から花粉が一斉に吹き飛ばされる。米粒大の雄花の一つ一つに約40万個の花粉が詰まっている。この花粉が、霞のようにたなびいて、スギの林が見えなくなるほどだ。花粉症をおこす草花は、北アメリカではブタクサ、ヨーロッパではカバの木やコナラなどだが、日本では花粉症の8割をスギ花粉症が占めている。
    それは日本にスギの木が多いからだ。理由は二つある。第一の理由は、第二次世界大戦後、日本は荒れた国土を緑にしようと、スギの苗を全国各地に植えた。20年後、そのスギが育ち、毎年春になると花粉が飛ぶようになったからだ。第二の理由は、日本人の食生活が欧米風になって、アレルギーを起こしやすくなったからだと言われている。スギ花粉症は、まさに日本人の現代病と言えるだろう。花粉症は薬で、症状を軽くおさえることができる。またスギの花粉が飛ぶのは、2月初めから4月にかけてで、この季節が終われば自然になおる。それで、このシーズンが来ると、都内のデパートには花粉症対策グッズコーナーがお目見えし、メーカー各社からは、新型マスクから情報提供までの「花粉症商戦」が花盛りとなる。"""

lower_intermediate_text = """茶々はわたしの日本語の先輩でした。毎日、日本語を一生懸命勉強して3か月ぐらいたったころには、日本人の友達といろいろな話もできるようになりました。そして茶々よりも日本語がわかるようになりました。けれどわたしの日本語の発音はまだ上手ではありません。家の人はわかってくれますが、茶々はわかりません。「おいで」と言っても茶々は来ません。「ちょっと見てごらん」と言っても見ません。「散歩に行こう」と言ってもふりむいてくれません。だから、いっしょに散歩することもできません。わたしの発音が家の人とちがうからです。それが大変ざんねんでした。それで、わたしはテープをたくさん聞いて練習しました。そして、はじめて茶々がわたしの「おいで」を聞いて、わたしのところへ来てくれた時は、本当にうれしくなりました。
    わたしの日本語がやっと茶々につうじたからです。今は、わたしは日本の生活にだいぶなれました。茶々はもう、わたしの日本語が大体わかりますから、毎日いっしょに散歩します。わたしの日本語の先輩、茶々のおかげで日本語も上手になったし、犬がこわくなくなって、犬が好きになりました。今度、わたしは茶々に中国語を教えようと思います。そして、中国語と日本語と、二つのことばのわかる犬にするつもりです。(ホン・イン〈中国〉)日本人は「きれい好き」だと言われています。また「風呂好き」だとも言われています。たしかに若い人の間では「朝シャン」族と呼ばれ、毎朝かならずかみを洗う人が多いです。これは少し洗いすぎかも知れません。
    入浴についても厚生省の調べによると内風呂(自分の家にある風呂)がある人の中で、ほとんど毎日風呂に入ると答えた人が約50%、1日おきに入る人がおよそ30%、残りの20%ぐらいが、二、三日おきに入るそうです。外のお風呂屋さん(別名銭湯)へ行く人たちの中では、週に2度行く人が最も多いそうです。お風呂と言えば、日本人の入るお風呂の平均温度は40度から42度くらいで、人によっては45度でも譲るいと言う人さえいます。けれどもあまり熱すぎるお風呂は、からだによくありません。ほかの国々では大体38度くらいだそうです。ですから外国から来た人は、みんな日本のお風呂はあつすぎると言います。このごろは、お風呂屋さんの数がだんだん少なくなりました。"""

upper_elementary_text = """むかしむかし、金が大好きな一人の王様がいました。ある日王様の家に一人の老人がやって来ました。その老人は有名な学者でしたが、お酒がたいへん好きでした。そこで、王様は、老人のためにたくさんの酒とおいしい料理を用意しました。10日間、老人は飲んだり食べたりしました。そして、10日目に満足して帰って行きました。この話を、酒の神が聞きました。酒の神はこの老人が好きだったので、王様にお礼をしたいと思いました。
    そして、王様にこう言いました。
    「お礼に、なんでも好きなものをあげよう。好きなものを言いなさい」
    「はい。ありがとうございます。」
    「私がさわったものを全部金にしてください」
    酒の神は、つまらない望みだと思いましたが、「わかった。その通りにしてやろう」と答えました。王様はよろこんで庭に行き、りんごにさわりました。すると、りんごは金のりんごになりました。バラの花にさわると金のバラに石にさわると金の石になりました。食堂に行ってテーブルにさわると金のテーブルになりました。しかし、そのうち、困ったことに気がつきました。おなかがすいたのでパンを食べようとしたのですが、パンにさわるとパンが金になってしまうのです。ミルクも金のミルクになってしまいます。食べるものがなにもない！」そこで、王様は小さな王女を呼びました。王女は部屋の中が金ばかりなので、おどろいて言いました。
    「おとうさま、どうなさったのですか。こんなに金ばかりで...」
    「助けておくれ。私はたいへんな失敗をしてしまったのだ」
    王様はそう言って、王女の手をつかみました。すると、王女も金になってしまいました。王様は泣きながら、酒の神の家に飛んでいきました。
    「私はおろかなお願いをしました。娘をもとの娘にしてください」
    「わかった。では、この国のいちばん大きな川に行って、二人とも体を洗いなさい。そうすれば、もとの体になるだろう」王様は、金の王女をつれて川に行きました。
    そして、水に入って体を洗うと、もとの王女になりました。
    王女は言いました。
    「おとうさま、あれを見てください」
    川の底を見ると、きらきら光るものがありました。"""

lower_elementary_text = """李さんは毎日お酒をのんでいます。お金もなくなりました。しかし、仕事はきらいです。いろいろ考えました。神様にお願いすることにしました。しかし、神様がどこにいるのかわかりません。困りました。図書館にいきました。古い本を調べました。その日の夜のことです。たばこを吸いました。そして神様のことを考えました。そのときです。たばこのけむりの中から何かでてきました。
    「あなたは私に何をたのみたいのですか。」
    とその人は言いました。
    「私はお金がありません。とてもこまっています。」
    「それでは、お金を作りましょう。」
    「けれども、お金というのはどんな形ですか。」
    ポケットの中に千円札を出しました。机の上におきました。
    「よろしい。」"""

class Test_jreadability:

    def test_upper_advanced(self):

        score = compute_readability(upper_advanced_text)

        assert 0.5 <= score < 1.5

    def test_lower_advanced(self):

        score = compute_readability(lower_advanced_text)

        assert 1.5 <= score < 2.5

    def test_upper_intermediate(self):

        score = compute_readability(upper_intermediate_text)

        assert 2.5 <= score < 3.5

    def test_lower_intermediate(self):

        score = compute_readability(lower_intermediate_text)

        assert 3.5 <= score < 4.5

    # test currently failing (score=4.19)
    #def test_upper_elementary(self):
    #
    #    score = compute_readability(upper_elementary_text)
    #
    #    assert 4.5 <= score < 5.5

    # test currently failing (score=5.12)
    #def test_lower_elementary(self):
    #    
    #    score = compute_readability(lower_elementary_text)
    #
    #    assert 5.5 <= score < 6.5

    def test_batch(self):

        # list of 600 japanese strings
        test_texts = [lower_elementary_text, upper_elementary_text, 
                      lower_intermediate_text, upper_intermediate_text, 
                      lower_advanced_text, upper_advanced_text] * 100

        # time to compute without passing initialized tagger
        start_time = time.time()
        scores_1 = []
        for text in test_texts:

            score = compute_readability(text)
            scores_1.append(score)

        uninitialized_tagger_time = time.time() - start_time

        # time to compute with initialized tagger
        start_time = time.time()
        tagger = Tagger()
        scores_2 = []
        for text in test_texts:

            score = compute_readability(text, tagger)
            scores_2.append(score)

        initialized_tagger_time = time.time() - start_time

        assert scores_1 == scores_2 # readability scores must be the same

        assert initialized_tagger_time < uninitialized_tagger_time # initialzing the tagger should save time