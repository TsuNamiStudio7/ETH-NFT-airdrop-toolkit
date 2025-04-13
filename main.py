from snapshot import get_nft_holders
from airdrop import send_airdrop

def main():
    print("🔍 Taking snapshot of NFT holders...")
    recipients = get_nft_holders()
    print(f"📋 {len(recipients)} addresses found.")
    
    confirm = input("⚠️ Proceed with airdrop? (yes/no): ")
    if confirm.lower() == "yes":
        send_airdrop(recipients)
    else:
        print("❌ Airdrop cancelled.")

if __name__ == "__main__":
    main()
