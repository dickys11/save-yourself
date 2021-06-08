package com.example.saveyourself

import android.app.DownloadManager
import android.telecom.Call
import java.io.IOException
import javax.security.auth.callback.Callback

class MainActivity : androidx.appcompat.app.AppCompatActivity() {

    private val client = okhttp3.OkHttpClient()

    override fun onCreate(savedInstanceState: android.os.Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        run("http://34.87.19.67:8888/getstatus/(username)/(numpage)")
    }

    private fun run(url: String) {
        val request = android.app.DownloadManager.Request.Builder()
            .url(url)
            .build()

        client.newCall(request).enqueue(object : Callback {
            fun onFailure(call: Call, e: IOException) {}
            fun onResponse(call: Call, response: okhttp3.Response) = println(response.body()?.string())
        })
    }
}
