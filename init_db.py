from app.database import Base, engine
from app.models import Role, AssetType
from app.utils import get_password_hash
import sys

def create_roles(db):
    roles = [
        {"name": "Admin"},
        {"name": "Manager"},
        {"name": "Employee"}
    ]
    for role_data in roles:
        role = Role(**role_data)
        db.add(role)
    db.commit()

def create_asset_types(db):
    asset_types = [
        {"name": "Computer"},
        {"name": "Monitor"},
        {"name": "Printer"},
        {"name": "Docking Station"}
    ]
    for asset_type_data in asset_types:
        asset_type = AssetType(**asset_type_data)
        db.add(asset_type)
    db.commit()

def create_it_asset_types(db):
    asset_types = [
        AssetType(name="Laptop", description="Portable computers"),
        AssetType(name="Desktop", description="Stationary computers"),
        AssetType(name="Router", description="Network routing devices"),
        AssetType(name="Switch", description="Network switching devices"),
        AssetType(name="Server", description="Data center servers"),
        AssetType(name="Storage", description="Data storage devices"),
        AssetType(name="Firewall", description="Network security devices"),
        AssetType(name="Keyboard", description="Input devices"),
        AssetType(name="Mouse", description="Input devices"),
    ]
    for asset_type_data in asset_types:
        asset_type = AssetType(**asset_type_data.__dict__)
        db.add(asset_type)
    db.commit()

def create_demo_user(db):
    from app.database import SessionLocal
    from app.models import User
    
    db = SessionLocal()
    try:
        # Create admin role if it doesn't exist
        admin_role = db.query(Role).filter(Role.name == "Admin").first()
        if admin_role is None:
            admin_role = Role(name="Admin")
            db.add(admin_role)
            db.commit()
            db.refresh(admin_role)

        # Create demo admin user
        demo_user = User(
            username="admin",
            email="admin@example.com",
            full_name="Admin User",
            hashed_password=get_password_hash("admin123"),
            role_id=admin_role.id
        )
        db.add(demo_user)
        db.commit()
        print("\nDemo admin user created:")
        print("Username: admin")
        print("Password: admin123")
    except Exception as e:
        print(f"Error creating demo user: {e}")
    finally:
        db.close()

def create_demo_assets(db):
    from app.database import SessionLocal
    from app.models import Asset, AssetStatus, User, AssetType
    
    db = SessionLocal()
    try:
        admin_user = db.query(User).filter(User.username == "admin").first()
        laptop_asset_type = db.query(AssetType).filter(AssetType.name == "Laptop").first()
        printer_asset_type = db.query(AssetType).filter(AssetType.name == "Printer").first()

        laptop = Asset(
            name="Dell XPS 13",
            description="13-inch laptop with i7 processor",
            serial_number="LAP123456",
            asset_type=laptop_asset_type,
            assigned_to=admin_user,
            assigned_at=datetime.now(),
            status=AssetStatus.IN_USE,
            purchase_date=datetime.now() - timedelta(days=30),
            warranty_expires=datetime.now() + timedelta(days=365),
            location="IT Department"
        )

        printer = Asset(
            name="HP LaserJet Pro",
            description="Laser printer with network capabilities",
            serial_number="PRN78910",
            asset_type=printer_asset_type,
            status=AssetStatus.AVAILABLE,
            purchase_date=datetime.now() - timedelta(days=180),
            warranty_expires=datetime.now() + timedelta(days=180),
            location="Conference Room"
        )

        db.add_all([laptop, printer])
        db.commit()
    except Exception as e:
        print(f"Error creating demo assets: {e}")
    finally:
        db.close()

def create_demo_maintenance(db):
    from app.database import SessionLocal
    from app.models import Asset, MaintenanceRecord
    
    db = SessionLocal()
    try:
        laptop = db.query(Asset).filter(Asset.name == "Dell XPS 13").first()

        maintenance1 = MaintenanceRecord(
            asset=laptop,
            maintenance_date=datetime.now() - timedelta(days=15),
            next_maintenance=datetime.now() + timedelta(days=90),
            notes="Annual maintenance completed",
            performed_by="IT Tech"
        )

        db.add(maintenance1)
        db.commit()
    except Exception as e:
        print(f"Error creating demo maintenance: {e}")
    finally:
        db.close()

def create_demo_asset_transfer(db):
    from app.database import SessionLocal
    from app.models import Asset, AssetTransfer, User
    
    db = SessionLocal()
    try:
        printer = db.query(Asset).filter(Asset.name == "HP LaserJet Pro").first()
        admin_user = db.query(User).filter(User.username == "admin").first()

        transfer = AssetTransfer(
            asset=printer,
            from_user=admin_user,
            to_user=admin_user,
            transfer_date=datetime.now() - timedelta(days=30),
            notes="Moved printer to conference room"
        )

        db.add(transfer)
        db.commit()
    except Exception as e:
        print(f"Error creating demo asset transfer: {e}")
    finally:
        db.close()

def main():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    
    from app.database import SessionLocal
    db = SessionLocal()
    try:
        print("\nCreating roles...")
        create_roles(db)
        
        print("\nCreating asset types...")
        create_asset_types(db)
        
        print("\nCreating demo admin user...")
        create_demo_user(db)
        
        print("\nDatabase initialization complete!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
