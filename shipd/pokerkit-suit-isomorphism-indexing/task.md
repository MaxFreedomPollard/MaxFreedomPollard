Add HandIndexer, exported in pokerkit.__all__, for indexing round-partitioned deals up to one global suit renaming.

HandIndexer(card_counts, deck=Deck.STANDARD) takes a nonempty iterable of positive int round sizes fitting within the selected Deck member. A deal for round r is a Card sequence or a string in Card.parse notation containing rounds 0 to r, with order free within each round. size(r), index(cards, r), unindex(i, r) and count(i, r) return, respectively, the class count, a deal's class number, any tuple of Cards representing class i, and that class's number of distinct deals.

Add Poker.hand_indexer using the per-street sums of hole and board cards as round sizes.

Add State.get_hand_index(player_index, street_index=None, board_index=0) and HandHistory.get_hand_indices(player_index, board_index=0). State indexes the player's hole cards and selected board in their original street groups through street_index; None selects the latest street dealt to any player or board. Complete showdown corrections replace cards in their dealt positions; partial shows retain known unshown cards. History returns one index per dealt street, using None for unknown or incomplete required cards; State raises ValueError in those cases.

Use ValueError for argument validation and draw games; integer arguments require ints in range excluding bool.
