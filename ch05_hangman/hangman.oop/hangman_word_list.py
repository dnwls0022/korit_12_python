word_list = [
    # 과일 & 채소 (Fruits & Vegetables)
    'apple', 'banana', 'cherry', 'durian', 'elderberry', 'fig', 'grape', 'honeydew', 'imbe', 'jackfruit',
    'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine',
    'ugli', 'vanilla', 'watermelon', 'xigua', 'yam', 'zucchini', 'tomato', 'potato', 'carrot', 'onion',
    'garlic', 'ginger', 'broccoli', 'cabbage', 'spinach', 'pepper', 'eggplant', 'radish', 'cucumber', 'lettuce',

    # 동물 (Animals)
    'ant', 'bear', 'cat', 'dog', 'elephant', 'frog', 'giraffe', 'horse', 'iguana', 'jellyfish',
    'kangaroo', 'lion', 'monkey', 'newt', 'owl', 'penguin', 'quail', 'rabbit', 'snake', 'tiger',
    'urchin', 'vulture', 'whale', 'xrayfish', 'yak', 'zebra', 'dolphin', 'shark', 'octopus', 'crab',
    'lobster', 'shrimp', 'turtle', 'lizard', 'parrot', 'eagle', 'chicken', 'sheep', 'goat', 'cow',
    'panda', 'koala', 'sloth', 'otter', 'beaver', 'walrus', 'hamster', 'squirrel', 'deer', 'wolf',

    # 직업 (Jobs)
    'actor', 'baker', 'chef', 'doctor', 'engineer', 'farmer', 'guard', 'hunter', 'innkeeper', 'judge',
    'knight', 'lawyer', 'miner', 'nurse', 'officer', 'pilot', 'queen', 'rancher', 'sailor', 'teacher',
    'umpire', 'vet', 'writer', 'artist', 'dancer', 'singer', 'coach', 'dentist', 'driver', 'worker',

    # 사물 & 가구 (Objects & Furniture)
    'alarm', 'bed', 'chair', 'desk', 'eraser', 'fan', 'glass', 'hammer', 'ink', 'jar',
    'key', 'lamp', 'mirror', 'notebook', 'oven', 'pen', 'quilt', 'radio', 'sofa', 'table',
    'umbrella', 'vase', 'watch', 'xylophone', 'yoyo', 'zipper', 'camera', 'phone', 'laptop', 'bottle',
    'window', 'door', 'pillow', 'blanket', 'candle', 'basket', 'button', 'clock', 'hammer', 'spoon',

    # 자연 & 날씨 (Nature & Weather)
    'beach', 'cloud', 'desert', 'earth', 'forest', 'glacier', 'hill', 'island', 'jungle', 'lake',
    'mountain', 'ocean', 'plain', 'river', 'stream', 'tree', 'valley', 'water', 'air', 'wind',
    'storm', 'rain', 'snow', 'sun', 'moon', 'star', 'planet', 'galaxy', 'cosmos', 'fire',

    # 기타 재미있는 단어들 (Mix) - 여기서부터 400개까지 쭉 채워집니다!
    'ability', 'absent', 'academy', 'accent', 'accept', 'access', 'accident', 'account', 'accurate', 'achieve',
    'acid', 'acoustic', 'acquire', 'across', 'action', 'active', 'actor', 'actual', 'adapt', 'add',
    'addict', 'address', 'adjust', 'admit', 'adult', 'advance', 'advice', 'aerobic', 'affair', 'afford',
    'afraid', 'again', 'age', 'agent', 'agree', 'ahead', 'aim', 'air', 'airport', 'aisle',
    'alarm', 'album', 'alcohol', 'alert', 'alien', 'alike', 'alive', 'all', 'allow', 'almost',
    'alone', 'alpha', 'already', 'also', 'alter', 'always', 'amaze', 'ambition', 'amount', 'amuse',
    'analyst', 'anchor', 'ancient', 'anger', 'angle', 'angry', 'animal', 'ankle', 'announce', 'annual',
    'another', 'answer', 'antenna', 'antique', 'anxiety', 'any', 'apart', 'apology', 'appear', 'apple',
    'approve', 'april', 'arch', 'arctic', 'area', 'arena', 'argue', 'arm', 'armed', 'armor',
    'army', 'around', 'arrange', 'arrest', 'arrive', 'arrow', 'art', 'article', 'artist', 'as',
    'ash', 'aside', 'ask', 'aspect', 'assault', 'asset', 'assist', 'assume', 'asthma', 'athlete',
    'atom', 'attack', 'attend', 'attitude', 'attract', 'auction', 'audit', 'august', 'aunt', 'author',
    'auto', 'autumn', 'average', 'avocado', 'avoid', 'awake', 'aware', 'away', 'awesome', 'awful',
    'awkward', 'axis', 'baby', 'bachelor', 'bacon', 'badge', 'bag', 'balance', 'balcony', 'ball',
    'bamboo', 'banana', 'banner', 'bar', 'bare', 'bargain', 'barrel', 'base', 'basic', 'basket',
    'battle', 'beach', 'bean', 'beauty', 'because', 'become', 'beef', 'before', 'begin', 'behave',
    'behind', 'believe', 'below', 'belt', 'bench', 'benefit', 'best', 'betray', 'better', 'between',
    'beyond', 'bicycle', 'bid', 'bike', 'bind', 'biology', 'bird', 'birth', 'bitter', 'black',
    'blade', 'blame', 'blanket', 'blast', 'bleak', 'bless', 'blind', 'blood', 'blossom', 'blue',
    'blur', 'blush', 'board', 'boat', 'body', 'boil', 'bomb', 'bone', 'bonus', 'book',
    'boost', 'border', 'boring', 'borrow', 'boss', 'bottom', 'bounce', 'box', 'boy', 'bracket',
    'brain', 'brake', 'branch', 'brass', 'brave', 'bread', 'breeze', 'brick', 'bridge', 'brief',
    'bright', 'bring', 'brisk', 'broccoli', 'broken', 'bronze', 'broom', 'brother', 'brown', 'brush',
    'bubble', 'buddy', 'budget', 'buffalo', 'build', 'bulb', 'bulk', 'bullet', 'bundle', 'bunker',
    'burden', 'burger', 'burst', 'bus', 'business', 'busy', 'butter', 'buyer', 'buzz', 'cabbage',
    'cabin', 'cable', 'cactus', 'cage', 'cake', 'call', 'calm', 'camera', 'camp', 'can',
    'canal', 'cancel', 'candy', 'cannon', 'canoe', 'canvas', 'canyon', 'capable', 'capital', 'captain',
    'car', 'carbon', 'card', 'cargo', 'carpet', 'carry', 'cart', 'case', 'cash', 'casino',
    'castle', 'casual', 'cat', 'catalog', 'catch', 'category', 'cattle', 'cause', 'caution', 'cave',
    'ceiling', 'celery', 'cell', 'census', 'century', 'cereal', 'certain', 'chair', 'chalk', 'champion',
    'change', 'chaos', 'chapter', 'charge', 'charity', 'chart', 'chase', 'cheap', 'check', 'cheese',
    'chef', 'cherry', 'chess', 'chest', 'chicken', 'chief', 'child', 'chimney', 'china', 'chip',
    'choice', 'choose', 'chronic', 'chuckle', 'chunk', 'churn', 'cider', 'cigarette', 'cinema', 'circle',
    'citizen', 'city', 'civil', 'claim', 'clap', 'clarify', 'claw', 'clay', 'clean', 'clerk',
    'clever', 'click', 'client', 'cliff', 'climb', 'clinic', 'clip', 'clock', 'clog', 'close',
    'cloth', 'cloud', 'clown', 'club', 'clump', 'cluster', 'clutch', 'coach', 'coast', 'coconut',
    'code', 'coffee', 'coil', 'coin', 'collect', 'color', 'column', 'combine', 'come', 'comfort',
    'comic', 'common', 'company', 'compass', 'compile', 'confirm', 'congrat', 'connect', 'consider', 'control'
]