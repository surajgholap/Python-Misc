def IsTrusted(node, trustGraph, pretrustedPeers, trustThreshold):
    if node in pretrustedPeers:
        return True
    for i in pretrustedPeers:
        for j in range(len(trustGraph)):
            if trustGraph[j][i] <= trustThreshold and trustGraph[j][i] != 0:
                return True
    return False


node = 0
trustGraph = [[0, 2], [2, 0]]
pretrustedPeers = [1]
trustThreshold = 1
print(IsTrusted(node, trustGraph, pretrustedPeers, trustThreshold))
