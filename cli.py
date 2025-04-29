import argparse
from tabulate import tabulate
from db import SessionLocal, init_db
from models import Card

def list_cards(session):
    cards = session.query(Card).all()
    table = [(c.id, c.name, c.set_name, c.rarity) for c in cards]
    print(tabulate(table, headers=["ID","Name","Set","Rarity"]))

def add_card(session, name, set_name, rarity):
    card = Card(name=name, set_name=set_name, rarity=rarity)
    session.add(card)
    session.commit()
    print(f"Added: {card}")

def delete_card(session, card_id):
    card = session.query(Card).get(card_id)
    if not card:
        print("No card found with that ID.")
    else:
        session.delete(card)
        session.commit()
        print(f"Deleted: {card}")

def main():
    parser = argparse.ArgumentParser(prog="cards")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list", help="List all cards")

    p_add = sub.add_parser("add", help="Add a new card")
    p_add.add_argument("name")
    p_add.add_argument("set_name")
    p_add.add_argument("rarity")

    p_del = sub.add_parser("delete", help="Delete card by ID")
    p_del.add_argument("id", type=int)

    args = parser.parse_args()
    session = SessionLocal()

    if args.cmd == "list":
        list_cards(session)
    elif args.cmd == "add":
        add_card(session, args.name, args.set_name, args.rarity)
    elif args.cmd == "delete":
        delete_card(session, args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    init_db()
    main()
