from chunker.features_extractors.feature_extractor import FeatureExtractor


class Organizations(FeatureExtractor):
    def __init__(self, organizations="../data/orgs"):
        with open(organizations) as f:
            lines = f.readlines()

        lines = map(str.strip, lines)
        self.organizations = set(lines)

    def extract(self, sentence, i, history):
        sentence, i, history = self.pad(sentence, i, history)

        word, pos = sentence[i]

        prevword, prevpos = sentence[i - 1]
        nextword, nextpos = sentence[i + 1]

        return {
            "org": word in self.organizations,
            "prevorg": prevword in self.organizations,
            "nextorg": nextword in self.organizations
        }
