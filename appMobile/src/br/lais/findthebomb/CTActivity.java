package br.lais.findthebomb;

import android.os.Bundle;
import android.app.Activity;
import android.view.View;
import android.widget.Chronometer;

public class CTActivity extends Activity {

	Chronometer chrono;
	
	/** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ct);
        
        chrono = (Chronometer) findViewById(R.id.chronometer1);
        
    }

    public void startChronometer(View view) {
    	chrono.start();
    }

    public void stopChronometer(View view) {
        chrono.stop();
    }

}
