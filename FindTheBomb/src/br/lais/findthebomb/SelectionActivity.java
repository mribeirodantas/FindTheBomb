package br.lais.findthebomb;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;

public class SelectionActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_selection);
		
	}
	
	public void entrarCTMode(View view){
		Intent i = new Intent(this, CTActivity.class);
		startActivity(i);
	}
	
	public void entrarTerrorMode(View view){
		Intent i = new Intent(this, TerrorActivity.class);
		startActivity(i);
	}


	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.selection, menu);
		return true;
	}

}
