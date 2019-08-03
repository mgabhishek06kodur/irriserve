package com.example.lenovo.irriserve;

import android.content.Intent;
import android.os.CountDownTimer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class login extends AppCompatActivity {
    EditText Name;
    EditText Password;
    TextView Info;
    Button Login;
    int counter=5;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        Name = (EditText)findViewById(R.id.ed1);
        Password = (EditText)findViewById(R.id.pwd);
        Info = (TextView)findViewById(R.id.t1);
        Login = (Button)findViewById(R.id.b1);

        Info.setText("No. of attempts remaining : 5");

        Login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(Name.getText().toString().equals("admin")&&Password.getText().toString().equals("1234")){;
                    Intent intent=new Intent(login.this,dashboard.class);
                    startActivity(intent);
                }
                else{
                    counter--;
                    Info.setText("No.of attempts remaining: "+String.valueOf(counter));
                    if(counter==0){
                        Login.setEnabled(false);
                        counter=5;
                        Toast alert = Toast.makeText(login.this, "Login Disabled for 30 seconds", Toast.LENGTH_SHORT);
                        alert.show();
                        new CountDownTimer(30000, 1000) {
                            public void onTick(long millisUntilFinished) {
                                Info.setText("seconds remaining: " + millisUntilFinished / 1000);
                            }
                            public void onFinish() {
                                Info.setText("done!");
                                Login.setEnabled(true);
                            }
                        }.start();
                    }
                }
            }

        });

    }
}
