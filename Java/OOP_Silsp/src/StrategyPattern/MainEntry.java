package StrategyPattern;

public class MainEntry {
	public static void main(String[] args) {
Character character = new Character();
		
		character.doAttack();
		character.setWeapon(new Gun());
		character.doAttack();
		character.setWeapon(new Knife());
		character.doAttack();
		character.setWeapon(new Kick());
		character.doAttack();
	}

}
