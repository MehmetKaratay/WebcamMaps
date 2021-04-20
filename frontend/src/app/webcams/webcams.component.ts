import { Component, OnInit } from '@angular/core';

@Component({
		selector: 'app-webcams',
		templateUrl: './webcams.component.html',
		styleUrls: ['./webcams.component.css']
})
export class WebcamsComponent implements OnInit {
		
		constructor() { }
		
		ngOnInit(): void {
		}

		webcam = 'Loch Morlich'
}
